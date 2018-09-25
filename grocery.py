
class Shopping_list:
    def __init__(self, title, description, grocery_items):
        self.title = title
        self.description = description
        self.grocery_items = grocery_items
    def display_list(self):
        print(" ")
        print("Displaying grocery list for {0}:\n".format(self.title))
        for items in self.grocery_items:
            print(items)
    def add_item(self, new_item):
        self.grocery_items.append(new_item)

class Grocery_item:
    def __init__(self, item_name):
        self.item_name = item_name
    def __repr__(self):
        return self.item_name

shopping_lists = []

def display_all_lists():
    print(" ")
    print("Current lists in memory: \n")
    for lists in shopping_lists:
        print(str(shopping_lists.index(lists) + 1) + ". " +lists.title + " - " + lists.description)
    print(" ")

def add_item(index):
    print("Add items, type 'q' when finished: \n")
    while True:
            item = input("Item to be added to list: ")
            if item == 'q':
                view = input("Exiting, would you like to view? y/n: ").lower()
                if view == 'y':
                    shopping_lists[index].display_list()
                    print(" ")
                    print('Returning to main menu...\n')
                    break
                elif view == 'n':
                    print(" ")
                    print('Returning to main menu...\n')
                    break
                else:
                    print("Invalid input, try again")  
            else:
                shopping_lists[index].add_item(Grocery_item(item))

print("Welcome to Kevin's Grocery list program!\n")

while True:

    print("Menu:\n")
    print("Press 'N' to create new list")
    print("Press 'A' to access existing list")
    print("Press 'D' to display lists:")
    print("Press 'Q' to quit\n")

    choice = input("What would you like to do? ").lower()
    if choice == 'q':
        print(" ")
        print('Goodbye!\n')
        break

    elif choice == 'n':
        print(" ")
        title = input("Enter title of list: ")
        desc = input("Enter description of list: ")
        print(" ")
        shopping_lists.append(Shopping_list(title, desc, []))
        list_index = len(shopping_lists) - 1
        add_item(list_index)

    elif choice == 'd':
        print(" ")
        if len(shopping_lists) == 0:
            print("There are no lists!\n")
        else:
            display_all_lists()

    elif choice == 'a':
        print(" ")
        if len(shopping_lists) == 0:
            print("There are no lists!\n")
        else:
            display_all_lists()

            while True:
                list_index = int(input("Enter number of the list you would like to view or modify items to: ")) -1
                if list_index + 1 > len(shopping_lists) or list_index < 0:
                    print(" ")
                    print("Error: list does not exist, try again!\n")
                else:
                    break
           
            while True:
                    print(" ")
                    print("Selected List: " + shopping_lists[list_index].title)
                    print(" ")
                    action = input("Press 'V' to view, 'A' to add items to list. or 'Q' to exit list ").lower()
                    print(" ")
                    if action == 'a':
                        add_item(list_index)
                    elif action == 'v':
                        shopping_lists[list_index].display_list()
                    elif action == 'q':
                        break
                    else:
                        print("Invalid Input, try again")
    else:
        print(" ")
        print("Invalid Input, try again!\n")






        

