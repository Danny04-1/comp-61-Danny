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
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
try:
    dog_img = pygame.image.load("dog_spritesheet.png").convert_alpha()  # Make sure your sprite sheet is correct
    dog_img = pygame.transform.scale(dog_img, (80, 80))  # Scale to desired size
except Exception as e:
    print("Error loading dog image:", e)
    sys.exit()

background_img = pygame.image.load("background2.png").convert()
title_img = pygame.image.load("Title.png")
title_img = pygame.transform.scale(title_img, (WIDTH, HEIGHT))
cone_img = pygame.Surface((50, 100), pygame.SRCALPHA)
pygame.draw.polygon(cone_img, (255, 165, 0), [(0, 100), (25, 0), (50, 100)])
bird_img = pygame.image.load("bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img, (60, 40))

# Load sounds
jump_sound = pygame.mixer.Sound("jump.wav")
point_sound = pygame.mixer.Sound("point.mp3")
lose_sound = pygame.mixer.Sound("game_over.mp3")
bg_music = "dog_runner_background.mp3"
pygame.mixer.music.load(bg_music)
pygame.mixer.music.play(-1)

# Dog class
class Dog(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        sprite_sheet = pygame.image.load("dog_spritesheet.png").convert_alpha()
        self.running_images = [sprite_sheet.subsurface(pygame.Rect(i * 64, 0, 64, 64)) for i in range(3)]
        self.jumping_image = sprite_sheet.subsurface(pygame.Rect(0, 64, 64, 64))
        self.crouching_image = sprite_sheet.subsurface(pygame.Rect(64, 64, 64, 64))

        self.image = self.running_images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.bottom = HEIGHT - 50  # Ensure dog is sitting on the ground

        self.jump_speed = 15
        self.gravity = 1
        self.velocity = 0
        self.is_jumping = False
        self.is_crouching = False
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.15

    def update(self):
        self.handle_animation()

        if self.is_jumping:
            self.velocity += self.gravity
            self.rect.y += self.velocity
            if self.rect.bottom >= HEIGHT - 50:  # Ensures dog doesn't fall below the ground
                self.rect.bottom = HEIGHT - 50
                self.is_jumping = False
                self.velocity = 0
        elif self.is_crouching:
            self.image = self.crouching_image
        else:
            # Animate running
            self.animation_timer += self.animation_speed
            if self.animation_timer >= 1:
                self.animation_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.running_images)
            self.image = self.running_images[self.frame_index]

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.velocity = -self.jump_speed
            self.image = self.jumping_image

    def crouch(self, is_crouching):
        if is_crouching:
            self.is_crouching = True
        else:
            self.is_crouching = False

    def handle_animation(self):
        if self.is_jumping:
            self.image = self.jumping_image
        elif self.is_crouching:
            self.image = self.crouching_image
        else:
            self.image = self.running_images[self.frame_index]


# Obstacle classes
class Cone(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        height = random.randint(60, 120)
        self.image = pygame.transform.scale(cone_img, (50, height))
        self.rect = self.image.get_rect(bottomleft=(x, HEIGHT))

    def update(self):
        self.rect.x -= 6
        if self.rect.right < 0:
            self.kill()

class Bird(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = bird_img
        y_pos = random.randint(HEIGHT - 200, HEIGHT - 150)
        self.rect = self.image.get_rect(topleft=(x, y_pos))

    def update(self):
        self.rect.x -= 6
        if self.rect.right < 0:
            self.kill()

# Button class
class Button:
    def __init__(self, text, pos, callback):
        self.text = text
        self.pos = pos
        self.callback = callback
        self.rect = pygame.Rect(pos[0], pos[1], 200, 50)

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect)
        label = font.render(self.text, True, WHITE)
        surface.blit(label, (self.rect.x + 10, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Splash screen
def splash_screen():
    alpha = 0
    fade_in = pygame.Surface((WIDTH, HEIGHT))
    fade_in.blit(title_img, (0, 0))
    for alpha in range(0, 255, 5):
        fade_in.set_alpha(alpha)
        screen.blit(fade_in, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)
    pygame.time.delay(1000)

# Instructions screen
def instructions():
    running = True
    while running:
        screen.fill(WHITE)
        lines = [
            "Press SPACE to jump (once only).",
            "Hold DOWN arrow to crouch under birds.",
            "Avoid construction cones and birds.",
            "Press ESC to return to the menu."
        ]
        for i, line in enumerate(lines):
            txt = small_font.render(line, True, BLACK)
            screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, 150 + i * 40))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

# Main menu
def main_menu():
    buttons = [
        Button("Start Game", (WIDTH // 2 - 100, 200), start_game),
        Button("Instructions", (WIDTH // 2 - 100, 300), instructions),
        Button("Quit", (WIDTH // 2 - 100, 400), sys.exit)
    ]
    while True:
        screen.blit(title_img, (0, 0))
        for button in buttons:
            button.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(event.pos):
                        button.callback()

# Game loop
def start_game():
    dog = Dog()
    obstacles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(dog)
    score = 0
    high_score = 0
    spawn_timer = 0
    game_active = True
    difficulty = 90

    while game_active:
        screen.blit(background_img, (0, 0))

        keys = pygame.key.get_pressed()
        dog.crouch(keys[pygame.K_DOWN])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dog.jump()

        # Spawn obstacle
        spawn_timer += 1
        if spawn_timer > difficulty:
            if random.random() < 0.6:
                obstacle = Cone(WIDTH + 100)
            else:
                obstacle = Bird(WIDTH + 100)
            obstacles.add(obstacle)
            all_sprites.add(obstacle)
            spawn_timer = 0
            difficulty = max(40, difficulty - 1)

        # Update
        all_sprites.update()

        # Collision
        if pygame.sprite.spritecollideany(dog, obstacles):
            lose_sound.play()
            game_active = False

        # Draw
        all_sprites.draw(screen)
        score += 1
        txt = font.render(f"Score: {score // 10}", True, BLACK)
        screen.blit(txt, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

    # Update high score
    high_score = max(high_score, score // 10)

    # Game over screen
    game_over_txt = font.render("Game Over!", True, BLACK)
    restart_txt = small_font.render("Press R to Restart or ESC for Menu", True, BLACK)
    while True:
        screen.fill(WHITE)
        screen.blit(game_over_txt, (WIDTH // 2 - game_over_txt.get_width() // 2, HEIGHT // 2 - 50))
        screen.blit(restart_txt, (WIDTH // 2 - restart_txt.get_width() // 2, HEIGHT // 2))
        high_txt = font.render(f"High Score: {high_score}", True, BLACK)
        screen.blit(high_txt, (WIDTH // 2 - high_txt.get_width() // 2, HEIGHT // 2 + 50))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_game()
                elif event.key == pygame.K_ESCAPE:
                    return


# Run the game
splash_screen()
main_menu()




