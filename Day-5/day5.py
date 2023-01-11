# For loop example:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)

# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
count = 0
for heights in student_heights:
    total_height += heights
    count += 1
average = total_height / count

print(round(average))

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# You are going to write a program that calculates the highest score from a List of scores.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# range
for number in range(1, 10):
  print(number)
# Does not print the last number in the range.

#  If you want to change the step size in a range method:
for number in range(1, 10, 3):
  print(number)

# Gauss' Math:
total = 0
for number in range(1, 101):
  total += number
print(total)

# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
         print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project: Password Generator 

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# pasword =""

# for char in range(1, nr_letters +  1):
#   password = random.choice(letters)

# for char in range(1, nr_numbers + 1):
#   password = random.choice(numbers)

# for char in range(1, nr_symbols + 1):
#   password = random.choice(symbols)

# print (password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list =[]

for char in range(1, nr_letters +  1):
  password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
