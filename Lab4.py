import random

def roll_die():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    rolls = []
    for _ in range(num_dice):
        rolls.append(roll_die())
    print("Rolled dice: {rolls}")
    return sum(rolls)

def get_round_result(player_total, computer_total):
    if player_total > computer_total:
        return "Win"
    elif player_total < computer_total:
        return "Loss"
    else:
        return "Draw"

def shop(score):
    while True:
        print("\nShop Menu:")
        print("1. Add +5 points (Cost: 5 points)")
        print("2. Add +15 points (Cost: 10 points)")
        print("3. Exit Shop")
        choice = input("Enter your choice: ")

        if choice == "1":
            if score >= 5:
                score += 5
                score -= 5
                print("You bought +5 points!")
            else:
                print("You dont have enough points.")
        elif choice == "2":
            if score >= 10:
                score += 15
                score -= 10
                print("You bought +15 points!")
            else:
                print("You dont haveenough points.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
    return score

def display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results):
    print("\n----- Game Summary -----")
    print(f"Total Rounds: {rounds}")
    print(f"Wins: {wins}, Draws: {draws}, Losses: {losses}")
    print(f"Final Score: {score}")

    print("\nRound History:")
    for i in range(rounds):
        print(f"Round {round_numbers}: Player {player_totals} vs Computer {computer_totals} -> {results}")

score = 0
rounds = 0
wins = 0
draws = 0
losses = 0
round_numbers = []
player_totals = []
computer_totals = []
results = []

while True:
    rounds += 1
    round_numbers.append(rounds)
    
    shop_choice = input("Do you want to visit the shop? (yes/no): ")
    if shop_choice == "yes":
        score = shop(score)
    
    print(f"\nRound {rounds}")
    player_total = roll_multiple_dice(2)
    computer_total = roll_multiple_dice(2)
    
    player_totals.append(player_total)
    computer_totals.append(computer_total)

    result = get_round_result(player_total, computer_total)
    results.append(result)

    if result == "Win":
        wins += 1
        score += 20
    elif result == "Draw":
        draws += 1
        score += 10
    elif result == "Loss":
        losses += 1

    print(f"Result: {result}, Current Score: {score}")

    continue_choice = input("Do you want to play another round? (yes/no): ")
    if continue_choice == "no":
        break

display_statistics(rounds, wins, draws, losses, score, round_numbers, player_totals, computer_totals, results)

