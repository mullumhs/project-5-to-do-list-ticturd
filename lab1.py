"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use lists in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a list named favorite_foods and add at least five different food items to it
favorite_foods = ["emit", "leon", "ward", "jenga", "bill"]

# Change the third item in the list to a different food
favorite_foods[2] = "sinclair"

# Print out only the first and fourth items in the list
print(favorite_foods[0])
print(favorite_foods[3])


# Ask the user for a food item
food = (input("Please enter a food to add to the list."))

# Append the user's food item to the list
favorite_foods.append(food)

# Print out the entire list of food items
for bitchunt in favorite_foods:
    print(bitchunt)
    