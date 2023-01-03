import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

# from the imported file `my_module`, we can call on that file with the variable/function within that file.
print(my_module.pi)

random_float = random.random()
print(random_float)

random_float_mult = random_float * 5
print(random_float_mult)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalized and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

import random

coin_flip = random.randint(0, 1)
if coin_flip == 0:
    print("Heads")
elif coin_flip == 1:
    print("Tails")


# Lists Examples:

item1 = "orange"
item2 = "lemon"
fruits = [item1, item2]
    # OR:
fruits_alternate = ["Cherry", "Lemon", "Orange"]

states_of_america = ["Delaware", "Pennsylvania", "New Mexico", "Texas", "Georgia", "Connecticut", "Maryland", "South Carolina", "Virginia", "Indiana"]

print(states_of_america[3])

# What if I want to change an item in a list?
states_of_america = ["Delaware", "Pennsylvania", "New Mexico", "Texas", "Georgia", "Connecticut", "Maryland", "South Carolina", "Virginia", "Indiana"]

states_of_america[1] = "Kansas"

# What if I want to extend the list?

states_of_america.append("Angelaland")

states_of_america.extend("Wiscansin")

print(states_of_america)

# Expected output: ['Delaware', 'Kansas', 'New Mexico', 'Texas', 'Georgia', 'Connecticut', 'Maryland', 'South Carolina', 'Virginia', 'Indiana']

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name





# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
