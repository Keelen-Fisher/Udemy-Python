# Conditional If/else

water_level = 50
if water_level > 80:
    print("Drain water!")
else:
    print("continue")

# Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2
bmi_cal = round(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi_cal}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi_cal}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi_cal}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi_cal}, you are obese.")
else:
    print(f"Your BMI is {bmi_cal}, you are clinically obese.")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Nested if/else conditional

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4

# **except** every year that is evenly divisible by 100

# **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small Pizza: $15

# Medium Pizza: $20

# Large Pizza: $25

# Pepperoni for Small Pizza: +$2

# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: + $1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill = 15
    if extra_cheese == "Y":
        bill += 1

if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}.")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.

# Then check for the number of times the letters in the word LOVE occurs.

# Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

two_strings = name1 + name2
lower_case = two_strings.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

z = int(str(true) + str(love))

if z < 10 or z > 90:
    print(f"Your score is {z}, you go together like coke and mentos.")
elif z >= 40 and z <= 50:
    print(f"Your score is {z}, you are alright together.")
else:
    print(f"Your score is {z}.")

 # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Treasure Choice Game:

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


choice = input(
    "You're at a cross road. Where do you want to go? Type 'left' or 'right'. \n")

if choice == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across. \n")
    if lake == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        if door == "red":
            print("You get burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!!")
        else:
            print("Wrong choice, Game Over.")
    else:
        print("You are attacked by a trout, Game Over.")
else:
    print("You go to a different direction and fall into a hole, Game Over.")
