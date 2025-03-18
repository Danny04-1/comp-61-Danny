print("\nWelcome to the List Operations Program!\n")
my_list = []
choice = 0
print (my_list)
while choice != 8:
    
    print("Welcome to the Menu, please select a command to continue:  ")
    print("1. Add a number to the list")
    print("2. Remove a number from the list")
    print("3. Insert a number at a specific position")
    print("4. Pop a number from the list")
    print("5. Find the sum, average, and maximum of the list")
    print("6. Search for a number in the list")
    print("7. Remove all odd numbers from the list")
    print("8. Exit")
    
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        a = 0
        a = int(input("Enter a number to add: "))
        index = 0
        counter = 0
        
        while (index < len(my_list)):
            if(my_list[index] == a):
                counter = counter + 1
            if(counter == 2):
                my_list.pop(index)
            index = index + 1
        my_list.append(a)
        print("Number has been added to the list: ", my_list)
    
    elif choice==2:
        print("What number would you like to remove?")
        print(my_list)
        rem_num = int(input("Enter the here:  "))
        if rem_num in my_list:
            my_list.remove(rem_num)
            print("This is the new list: ", my_list)
        
        else:
            print("Invalid Input. Please give me a Valid Input.")
    
    elif choice==3:
        pos = int(input("What numeric position would you like to put the number:  "))
        new_num = int(input("What number would you like in that spot?"))
        if pos < 0 or pos > len(my_list):
            print("Invalid position. Please enter a valid position.")
       
        else:
            my_list.insert(pos, new_num)
            print("This is the new list: ", my_list)
   
    elif choice ==4:
        print("What number would you like to pop?")
        print(my_list)
        pop_num = int(input("Please enter the number: "))
        index = 0
       
        while (index < len(my_list)):
            if(my_list[index] == pop_num):
                my_list.pop(index)
            index = index + 1
            print(my_list)
        print("Invalid Input. Please Enter a Valid Input.")
        print("This is the new list: ", my_list)
   
    elif choice ==5:
        summy = sum(my_list)
        avg = summy % len(my_list)
        maxx = max(my_list)
        print("The sum of the list is: ", summy,)
        print("The list's average number is: ", avg)
        print("The maximum number is: ", maxx)
   
    elif choice ==6:
        search = int(input("What number would you like to search: "))
        if search in my_list:
            index = my_list.index(search)
            print(search, "Is here: ")
       
        else:
            print("This number is not in the list.")
    
    elif choice ==7:
        no_odds = []
       
        for x in my_list:
            if x % 2 == 0:
                no_odds.append(x)
        my_list = no_odds
        print("This is the list with no odd numbers: ", my_list)
    
    elif choice ==8:
        print("\nMenu Exited\n")
    
    else:
        print("Please enter a Number Between 1 and 8.")
print("Goodbye\n")
