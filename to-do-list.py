"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: to-do-list.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import time
#make a list
#allow user to add variables to the list
#allow user to delete variables from the list
#allow user to edit the list

todolist = []


def menu():
    print("Please select an option:")
    print("1. Add something to the list")
    print("2. Delete something from the list")
    print("3. Edit something from the list")
    print("4. View list")



def choice():
    while True:
            try:
                choice = int(input())
                if choice == 1:
                    return choice
                if choice == 2:
                    return choice
                if choice == 3:
                    return choice
                if choice == 4:
                    return choice
                else:
                    print("Please enter a number between 1 and 3")

            except:
                print("Please enter a valid number.")

def add():
    print("What would you like to add to your list?")
    addtolist = input()
    todolist.append(addtolist)

def delete():
    print("What would you like to delete from your list?")
    deletefromlist = input()
    todolist.remove(deletefromlist)

def edit():
    print("What would you like to edit?")
    remove = todolist.index(input())

    print("Enter your replacement")
    add = input()

    todolist[remove] = add


def viewlist():
    for i, item in enumerate(todolist):
        print(f"{i + 1}. {item}")
        time.sleep(1)

while True:
    menu()
    ch = choice()
    if ch == 1:
        add()
    if ch == 2:
        delete()
    if ch == 3:
        edit()
    if ch == 4:
        viewlist()

    




