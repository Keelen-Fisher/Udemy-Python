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

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
name_count = len(names)
random_name = random.randint(0, name_count - 1)
random_choice = names[random_name]
print(f"{random_choice} is going to buy the meal today!")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Finding the length of a list:
states_of_america = ["Delaware", "Pennsylvania", "New Mexico", "Texas", "Georgia", "Connecticut", "Maryland", "South Carolina", "Virginia", "Indiana"]

print(len(states_of_america))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# How to combine lists
languages = ["Python", "Java", "JavaScript", "C++", "C#", "HTML", "CSS"]
errors = ["syntax", "type", "inline", "data"]

language_errors = [languages, errors]
print(language_errors)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:

# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']


row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

select_row = map[vertical -1]
select_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Day 4 Project: Create a Rock Paper Scissors Game Where the user goes against the computer. The computer inputs a random choice between rock, paper, and scissors.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

shoot = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
choice = int(shoot)
list_of_shoots = [rock, paper, scissors]
comp_shoots = len(list_of_shoots)
random_shoots = random.randint(0, comp_shoots - 1)
random_choice = list_of_shoots[random_shoots]

if choice == 0:
  print(rock)
  print(f"Computer chose: \n {random_choice}")
  if random_shoots == 0:
    print("Draw.")
  elif random_shoots == 1:
    print("You loose.")
  elif random_shoots == 2:
    print("You Win")
  
elif choice == 1:
  print(paper)
  print(f"Computer chose: \n {random_choice}")
  if random_shoots == 1:
    print("Draw.")
  elif random_shoots == 2:
    print("You loose.")
  elif random_shoots == 0:
    print("You Win")

elif choice == 2:
  print(scissors)
  print(f"Computer chose: \n {random_choice}")
  if random_shoots == 2:
    print("Draw.")
  elif random_shoots == 0:
    print("You loose.")
  elif random_shoots == 1:
    print("You Win")
else:
  print("Wrong input.")
