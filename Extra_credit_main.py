import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog Jumper")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
try:
    font = pygame.font.SysFont("Arial", 36)
    small_font = pygame.font.SysFont("Arial", 24)
except Exception as e:
    print(f"Error loading font: {e}")
    # Fallback font
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 32)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0) # Define Orange color

# --- Asset Loading ---
# Load images with error handling
def load_image(filename, convert_alpha=True, scale=None):
    """Loads an image, handles errors, optionally converts alpha and scales."""
    try:
        image = pygame.image.load(filename)
        if convert_alpha:
            image = image.convert_alpha()
        else:
            image = image.convert()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except pygame.error as e:
        print(f"Error loading image '{filename}': {e}")
        # Return a placeholder surface
        placeholder = pygame.Surface(scale if scale else (50, 50))
        placeholder.fill(ORANGE)
        return placeholder
    except FileNotFoundError:
         print(f"Error: File not found '{filename}'")
         placeholder = pygame.Surface(scale if scale else (50, 50))
         placeholder.fill(ORANGE)
         return placeholder

# Load Dog Spritesheet
# !! IMPORTANT: Ensure 'dog_spritesheet.png' exists in the correct location !!
sprite_sheet = load_image("dog_spritesheet2.png", convert_alpha=True)

# Load other images
background_img = load_image("background2.png", convert_alpha=False) # Backgrounds usually don't need alpha
title_img = load_image("Title.png", scale=(WIDTH, HEIGHT))
bird_img = load_image("bird.png", scale=(60, 40))

# Create Cone image programmatically
cone_img = pygame.Surface((50, 100), pygame.SRCALPHA) # Use SRCALPHA for transparency
pygame.draw.polygon(cone_img, ORANGE, [(0, 100), (25, 0), (50, 100)]) # Use defined ORANGE

# Load sounds with error handling
def load_sound(filename):
    """Loads a sound, handles errors."""
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error as e:
        print(f"Error loading sound '{filename}': {e}")
        return None # Return None if sound fails to load
    except FileNotFoundError:
         print(f"Error: File not found '{filename}'")
         return None

jump_sound = load_sound("jump.wav")
point_sound = load_sound("point.mp3") # Note: point_sound is loaded but not used
lose_sound = load_sound("game_over.mp3")
bg_music_file = "dog_runner_background.mp3" # Just store filename for now

# Function to safely play sounds
def play_sound(sound):
    if sound:
        sound.play()

# --- Dog class ---
# --- Dog class ---
class Dog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load the single dog image
        self.base_image = load_image("dog.png", convert_alpha=True, scale=(80, 80)) # Initial size
        self.image = self.base_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.bottom = HEIGHT

        # Movement variables
        self.jump_speed = 20
        self.gravity = 1
        self.velocity = 0
        self.is_jumping = False
        self.is_crouching = False

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.is_crouching = keys[pygame.K_DOWN] and not self.is_jumping

        # --- Vertical Movement (Jumping/Gravity) ---
        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity
            # Check for landing
            if self.rect.bottom >= HEIGHT:
                self.rect.bottom = HEIGHT
                self.is_jumping = False
                self.velocity = 0
                self.image = pygame.transform.scale(self.base_image, (80, 80)) # Reset size
                self.rect = self.image.get_rect(bottom=self.rect.bottom, centerx=self.rect.centerx)
        else:
            # Snap to ground if not jumping
            self.rect.bottom = HEIGHT
            if not self.is_crouching:
                self.image = pygame.transform.scale(self.base_image, (80, 80))
                self.rect = self.image.get_rect(bottom=self.rect.bottom, centerx=self.rect.centerx)
            else:
                self.image = pygame.transform.scale(self.base_image, (80, 50)) # Squashed for crouch
                self.rect = self.image.get_rect(bottom=self.rect.bottom, centerx=self.rect.centerx)


    def jump(self):
        # Allow jump only if on the ground
        if not self.is_jumping and self.rect.bottom >= HEIGHT:
            self.is_jumping = True
            self.velocity = -self.jump_speed
            play_sound(jump_sound)
            self.image = pygame.transform.scale(self.base_image, (90, 90)) # Slightly bigger when jumping
            self.rect = self.image.get_rect(bottom=self.rect.bottom, centerx=self.rect.centerx)


# --- Obstacle classes ---
class Cone(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        height = random.randint(60, 120)
        # Scale the base cone image correctly
        self.image = pygame.transform.scale(cone_img, (50, height))
        self.rect = self.image.get_rect(bottomleft=(x, HEIGHT)) # Position based on bottom left

    def update(self, dt): # Pass dt even if not used yet, good practice
        self.rect.x -= 360 * dt # Move based on pixels per second (e.g., 360 pixels/sec)
        if self.rect.right < 0:
            self.kill()

class Bird(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = bird_img # Already loaded and scaled
        # Fly slightly lower to be relevant for crouching
        y_pos = random.randint(HEIGHT - 120, HEIGHT - 70)
        self.rect = self.image.get_rect(topleft=(x, y_pos))

    def update(self, dt): # Pass dt
        self.rect.x -= 420 * dt # Birds are a bit faster (e.g., 420 pixels/sec)
        if self.rect.right < 0:
            self.kill()

# --- Button class ---
class Button:
    def __init__(self, text, pos, width, height, callback):
        self.text = text
        self.pos = pos
        self.width = width
        self.height = height
        self.callback = callback
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
        # Render text surface once
        self.label = font.render(self.text, True, WHITE)
        self.label_rect = self.label.get_rect(center=self.rect.center)
        # Add hover effect state
        self.is_hovered = False

    def draw(self, surface):
        # Change color on hover
        button_color = ORANGE if self.is_hovered else BLACK
        pygame.draw.rect(surface, button_color, self.rect, border_radius=5)
        surface.blit(self.label, self.label_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
                if self.callback:
                    self.callback() # Call the associated function


# --- Game States ---
def splash_screen():
    screen.blit(title_img, (0, 0)) # Show title immediately
    pygame.display.update()
    pygame.time.delay(2000) # Wait 2 seconds

def instructions():
    running = True
    instruction_lines = [
        "Instructions",
        "",
        "Press SPACE to Jump",
        "Hold DOWN arrow to Crouch",
        "Avoid cones and birds!",
        "",
        "Press ESC to return to Menu"
    ]
    rendered_lines = []
    line_height = font.get_height() + 10
    total_height = len(instruction_lines) * line_height
    start_y = (HEIGHT - total_height) // 2

    for i, line in enumerate(instruction_lines):
         if i == 0: # Title font
              txt_surf = font.render(line, True, BLACK)
         else: # Smaller font
              txt_surf = small_font.render(line, True, BLACK)
         txt_rect = txt_surf.get_rect(center=(WIDTH // 2, start_y + i * line_height))
         rendered_lines.append((txt_surf, txt_rect))


    while running:
        screen.fill(WHITE) # White background for instructions

        for surf, rect in rendered_lines:
            screen.blit(surf, rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False # Exit instructions loop

def main_menu():
    # Center buttons more reliably
    button_width = 250
    button_height = 60
    button_x = (WIDTH - button_width) // 2
    button_y_start = HEIGHT // 2 - 100
    button_spacing = 80

    buttons = [
        Button("Start Game", (button_x, button_y_start), button_width, button_height, start_game),
        Button("Instructions", (button_x, button_y_start + button_spacing), button_width, button_height, instructions),
        Button("Quit", (button_x, button_y_start + 2 * button_spacing), button_width, button_height, sys.exit)
    ]

    running = True
    while running:
        screen.blit(title_img, (0, 0)) # Draw background title

        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            button.check_hover(mouse_pos) # Update hover state
            button.draw(screen) # Draw button

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle button clicks via the button's method
            for button in buttons:
                button.handle_event(event)


# --- Main Game Loop ---
def start_game():
    dog = Dog()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(dog) # Dog should be in all_sprites too

    score = 0
    high_score = 0 # Load high score from file could be added here
    try:
        with open("highscore.txt", "r") as f:
            high_score = int(f.read())
    except (FileNotFoundError, ValueError):
        high_score = 0


    # Obstacle spawning parameters
    obstacle_spawn_timer = 0
    min_spawn_time = 0.8 # Minimum seconds between spawns
    max_spawn_time = 2.0 # Initial max seconds between spawns
    next_spawn_delay = random.uniform(min_spawn_time, max_spawn_time)
    spawn_time_reduction = 0.01 # How much max_spawn_time decreases per obstacle
    min_possible_spawn_time = 0.6 # Absolute minimum max_spawn_time can reach

    game_active = True
    game_over = False # State for game over screen

    # Start background music
    try:
        pygame.mixer.music.load(bg_music_file)
        pygame.mixer.music.play(-1) # Loop indefinitely
    except pygame.error as e:
        print(f"Error loading/playing music '{bg_music_file}': {e}")

    # Game loop
    while True: # Loop indefinitely until explicitly exited
        # Calculate delta time (time since last frame in seconds)
        dt = clock.tick(FPS) / 1000.0

        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not game_over: # Only handle game input if game is active
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_SPACE:
                         dog.jump()
            else: # Handle input on game over screen
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_r:
                         # Save high score before restarting
                         try:
                            with open("highscore.txt", "w") as f:
                                f.write(str(high_score))
                         except IOError:
                             print("Warning: Could not save high score.")
                         start_game() # Restart the game function
                     elif event.key == pygame.K_ESCAPE:
                         # Save high score before returning to menu
                         try:
                            with open("highscore.txt", "w") as f:
                                f.write(str(high_score))
                         except IOError:
                              print("Warning: Could not save high score.")
                         pygame.mixer.music.stop() # Stop music before menu
                         return # Exit start_game to return to main_menu

        # --- Game Logic ---
        if not game_over:
            # Update sprites
            all_sprites.update(dt) # Pass dt to all sprites

            # Spawn obstacles
            obstacle_spawn_timer += dt
            if obstacle_spawn_timer >= next_spawn_delay:
                obstacle_spawn_timer = 0 # Reset timer
                # Choose obstacle type
                if random.random() < 0.6: # 60% chance for cone
                    obstacle = Cone(WIDTH + 50) # Spawn slightly off screen right
                else:
                    # Spawn bird only if dog isn't currently near bird height
                    # This prevents impossible situations if dog is jumping high
                    if not (dog.is_jumping and dog.rect.top < HEIGHT - 150):
                         obstacle = Bird(WIDTH + 50)
                    else:
                         obstacle = Cone(WIDTH + 50) # Default to cone if bird spawn is risky

                obstacles.add(obstacle)
                all_sprites.add(obstacle)

                # Decrease spawn delay slightly to increase difficulty
                max_spawn_time = max(min_possible_spawn_time, max_spawn_time - spawn_time_reduction)
                next_spawn_delay = random.uniform(min_spawn_time, max_spawn_time)


            # Collision detection
            # Use mask collision for pixel-perfect checks if desired
            # if pygame.sprite.spritecollide(dog, obstacles, False, pygame.sprite.collide_mask):
            if pygame.sprite.spritecollideany(dog, obstacles): # Simpler rect collision
                play_sound(lose_sound)
                pygame.mixer.music.stop()
                game_over = True # Enter game over state
                high_score = max(high_score, int(score)) # Update high score


            # Update score
            score += dt * 10 # Increase score based on time survived


        # --- Drawing ---
        screen.blit(background_img, (0, 0)) # Draw background first
        all_sprites.draw(screen) # Draw all sprites (dog and obstacles)

        # Draw Score
        score_txt = font.render(f"Score: {int(score)}", True, BLACK)
        screen.blit(score_txt, (10, 10))

         # Draw High Score
        high_score_txt = font.render(f"High Score: {high_score}", True, BLACK)
        high_score_rect = high_score_txt.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(high_score_txt, high_score_rect)


        # --- Game Over Screen ---
        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((200, 200, 200, 180)) # Semi-transparent grey overlay
            screen.blit(overlay, (0,0))

            game_over_font = pygame.font.Font(None, 72) # Larger font for game over
            restart_font = pygame.font.Font(None, 40)

            game_over_text = game_over_font.render("Game Over!", True, BLACK)
            go_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            screen.blit(game_over_text, go_rect)

            final_score_text = restart_font.render(f"Your Score: {int(score)}", True, BLACK)
            fs_rect = final_score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
            screen.blit(final_score_text, fs_rect)

            restart_text = restart_font.render("Press R to Restart", True, BLACK)
            r_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 60))
            screen.blit(restart_text, r_rect)

            menu_text = restart_font.render("Press ESC for Menu", True, BLACK)
            m_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            screen.blit(menu_text, m_rect)


        # Update the display
        pygame.display.flip() # Use flip for potentially better performance

# --- Run the game ---
if __name__ == "__main__": # Good practice to put main execution in here
    splash_screen()
    main_menu()
    pygame.quit() # Clean up pygame when main_menu exits
    sys.exit()