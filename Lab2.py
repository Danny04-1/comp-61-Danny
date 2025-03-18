print("Welcome to Simple ATM Simulator\n")

balance = 1000.00
choice = 0  

while choice != 4:
    
    print("Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your current balance is: $",balance)

    elif choice == 2:
        deposit_amount = float(input("Enter amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount
            print("Deposit successful! Your new balance is: $",balance)
        else:
            print("Invalid input. Please enter a positive value.")

    elif choice == 3:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        elif withdraw_amount <= 0:
            print("Invalid amount. Please enter a positive value.")
        else:
            balance -= withdraw_amount
            print("Withdrawal successful! Your new balance is: $",balance)

    elif choice == 4:
        print("Thank you for using our ATM. Have a good day!")

    else:
        print("Please enter a number between 1 and 4.")
