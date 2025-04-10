import random

EMPTY = 0
SHIP = 1
HIT = -1
MISS = -2

GRID_SIZE = 10

def initialize_battlefield():
    """
    Creates and returns a 10x10 grid initialized to EMPTY (0).
    """
    GRID_SIZE = 10
    EMPTY = 0

    battlefield = []

    for row in range(GRID_SIZE):
        new_row = []  
        for col in range(GRID_SIZE):
            new_row.append(EMPTY)  
        battlefield.append(new_row)  

    return battlefield

def can_place_ship(battlefield, row, col, size, horizontal):
    """
    Returns True if a ship of a given size can be placed at the specified position.
    """
    if horizontal:
        if col + size > GRID_SIZE:
            return False
        for i in range(size):
            if battlefield[row][col + i] != EMPTY:
                return False
    else:
        if row + size > GRID_SIZE:
            return False
        for i in range(size):
            if battlefield[row + i][col] != EMPTY:
                return False
    return True

def place_ship(battlefield, row, col, size, horizontal):
    """
    Places a ship of a given size at the specified location on the battlefield.
    """
    for i in range(size):
        if horizontal:
            battlefield[row][col + i] = SHIP
        else:
            battlefield[row + i][col] = SHIP

def randomly_place_ships(battlefield):
    """
    Randomly places 6 ships on the battlefield.
    """
    ship_sizes = [2, 2, 3, 3, 5, 5]
    for size in ship_sizes:
        while True:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            horizontal = random.choice([True, False])
            if can_place_ship(battlefield, row, col, size, horizontal):
                place_ship(battlefield, row, col, size, horizontal)
                break

def display_battlefield(battlefield, reveal_ships=False):
    """
    Displays the battlefield to the console.
    """
    print("   " + " ".join(str(i) for i in range(GRID_SIZE)))
    for i, row in enumerate(battlefield):
        row_display = []
        for cell in row:
            if cell == HIT:
                row_display.append("H")
            elif cell == MISS:
                row_display.append("M")
            elif cell == SHIP and reveal_ships:
                row_display.append("S")
            else:
                row_display.append("~")
        print(f"{i:<2} " + " ".join(row_display))

def ships_remaining(battlefield):
    """
    Returns the number of ship segments still unhit.
    """
    return sum(row.count(SHIP) for row in battlefield)

def play_game():
    """
    Main game loop. Continues until all ships are sunk.
    """
    print("Welcome to Battleship!")
    print("Enter coordinates to attack (row and column between 0-9).")
    print("Enter -1 -1 to reveal all ships (cheat/debug mode).\n")
    
    battlefield = initialize_battlefield()
    randomly_place_ships(battlefield)
    
    while ships_remaining(battlefield) > 0:
        display_battlefield(battlefield)
        
        try:
            coords = input("Enter row and column: ").split()
            if len(coords) != 2:
                raise ValueError
            row, col = map(int, coords)
        except ValueError:
            print("Invalid input. Please enter two integers.")
            continue
        
        if row == -1 and col == -1:
            print("\n[DEBUG MODE] Revealing all ships:")
            display_battlefield(battlefield, reveal_ships=True)
            continue
        
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            print("Invalid coordinates. Try again.")
            continue
        
        if battlefield[row][col] == SHIP:
            battlefield[row][col] = HIT
            print("Hit!")
        elif battlefield[row][col] == EMPTY:
            battlefield[row][col] = MISS
            print("Miss!")
        else:
            print("You already attacked this location.")
    
    print("\nCongratulations! You sank all the ships!")
    print("Final battlefield:")
    display_battlefield(battlefield, reveal_ships=True)

if __name__ == "__main__":
    play_game()
