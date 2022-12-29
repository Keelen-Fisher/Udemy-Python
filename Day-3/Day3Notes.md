# Day 3

## Conditional Statements, Logical Operators, Code Blocks, and Scope

### [Example Code from Day 3](Day3.py)

### conditional if/else

- EX:

      if condition:
        do this
      else:
        do this

### Example of the logic of conditional statement, using the example of height requirements for a ride

![Example](../assets/if%20else%20conditional%20logic%20example.png)

- Solution to Example:

        print("Welcome to the rollercoaster!")
        height = int(input("What is your height in cm? "))

        if height > 120:
          print("You can ride the roller coaster!")
        else:
          print("Sorry, you have to grow taller before you can ride.")

- ***SIDE NOTE:*** Just like with JavaScript, when you are typing code, formatting especially with indentation is VERY important.

### More operations

- == -> Equal to

- != -> Not equal to

- % -> Modulo

- When you have one equal sign, you are ***Assigning*** something to a piece of data.

- When you are using two equal signs, you are ***Checking*** something to a piece of data.

### nested if/else

- Once the first condition is passed, we can check for another condition using another if/else condition inside of the first if statement.

- In order for this to be possible, the first if conditional statement needs to be ***true*** and the nested if statement needs to be ***false***.

### With that being said, here is an example of the ride requirements flow chart, expanded to a condition of age

![EX 2](../assets/if%20else%20conditional%20logic%20example%202.png)

- Solution to Example 2:

      print("Welcome to the rollercoaster!")
      height = int(input("What is your height in cm? \n"))

      if height >= 120:
        print("You can ride the roller coaster!")
        age = int(input("What is your age? \n"))
        if age <= 18: 
          print("Please pay $7.")
        else:
          print("Please Pay $12.")
      else:
        print("Sorry, you have to grow taller before you can ride.")

### Elif statement

- An extension of conditional statements

### Example of the ride requirements expanded by age range

![Alt text](../assets/if%20else%20conditional%20logic%20example%203.png)

- Solution to Example:

### Leap Year Example

- Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

- on every year that is evenly divisible by 4

- **except** every year that is evenly divisible by 100

- **unless** the year is also evenly divisible by 400

- Flow Chart Example:

![Alt text](../assets/Leap%20Year%20Example.png)

- Solution to Example:

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

### Multiple If conditions

- If you want to execute all of the conditions based on the fact that the condition is true, use multiple if conditions.

### Example of the ride requirements expanded by age range, and added options such as photos using multiple if statements

![Alt text](../assets/if%20else%20conditional%20logic%20example%204.png)

- Solution to the example:

      print("Welcome to the rollercoaster!")
      height = int(input("What is your height in cm? \n"))
      bill = 0

      if height >= 120:
        print("You can ride the roller coaster!")
        age = int(input("What is your age? \n"))
        if age < 12:
          bill = 5
          print("Child tickets are $5.")
        elif age <= 18: 
          bill = 7
          print("Youth tickets are $7.")
        else:
          bill = 12
          print("Adult tickets are $12.")

        wants_photo = input("Do you want a photo taken? Y or N. \n")
        if wants_photo == "Y":
          # Add $3 to their bill.
          bill += 3

        print(f"Your final bill {bill}")
        
      else:
        print("Sorry, you have to grow taller before you can ride.")

### Multiple conditions in the same line of code

#### We use logical operators

- A and B

- C or D

- not E

### Example of the ride requirements expanded by age range, and added options such as photos using multiple if statements, now including another age range between 45-55

- Solution:

      elif age >= 45 and age <= 55:
          print("Everything is going to be okay, have a free ride on us!")
