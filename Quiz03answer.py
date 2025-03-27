class MenuProgram:
    def __init__(self):
        self.item_list = []
        self.menu_option = 0

    def show_menu(self):
        print("1. Add item")
        print("2. Remove last item")
        print("3. Exit")
        self.menu_option = int(input("Pick one: "))
    
    def display_output(self):
        print("Current list:", self.item_list)
    
    def run(self):
        while self.menu_option != 3:
            self.show_menu()
            if self.menu_option == 1:
                item_name = input("Enter an item: ")
                self.item_list.append(item_name)
                self.display_output()
            elif self.menu_option == 2:
                if self.item_list:
                    self.item_list.pop()
                else:
                    print("List is empty, nothing to remove.")
                self.display_output()
 






#item_list=[]
#menu_option=0
#while(menu_option !=3):
#    print("1. add item")
#     print("2. add item")
#    menu_option=int(input("enter a option: "))
#
#if(menu_option==1):
#    item_name = (input("enter a item: "))
#    item_list.append(item_name)
#    print(item_list)
#
#if(menu_option==2):
#    item_list.pop()
#    print(item_list)


