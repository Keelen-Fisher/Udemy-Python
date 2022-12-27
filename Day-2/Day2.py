#Data Types
#Stings
print("Hello"[3])

# Integer
print(1290 + 34)

# Human Readable integers  
print(123_345_678)

# Float
print(3.1498454)

# Boolean
True
False

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# How to convert an integer to a string Example:

num_char = len(input("What is your name?"))

new_num_char = str(num_char)

print("Your name has" + new_num_char + " characters.")

# Convert integer to float:

a = float(123)

# Converting the string "100.5" to a float and then adding it to 70.
print(70 + float("100.5"))

# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#f-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") 


# EX: Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")

months = 12 
weeks = 52
days = 365

remaining_age = 90 - int(age)

x = remaining_age * days
y = remaining_age * weeks
z = remaining_age * months

print(f"You have {x} days, {y} weeks, and {z} months to live.")

# Day 2 Project Code:
# Create a tip calculator

print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip_percent = input("What percentage of tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tip_amount = int(tip_percent) * .01
tip_amount_dollar = tip_amount * int(total)
total_int = int(total)
total_due = (total_int + tip_amount_dollar) / int(num_people)
final_due = round(total_due, 2)
print(f"Each person should pay: ${final_due}")
