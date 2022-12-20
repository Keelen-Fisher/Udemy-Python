# Printing Functions:
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
# Combining two strings into one:
print('e.g. print("Hello " + "world")')
print("Hello" + "" + "Keelen")
print("New lines can be created with a backslash and n.")
# Example of using \n for a new line:
print("Hello World!\nThis is a new line")

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# input functions
input("What is your name?")
# Print Concatenation with input
print("Hello" + input("What is your name?"))
# Printing the length of the output:
print( len( input("What is your name? ") ) )

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Variable Reassignment
name = "Keelen"
print(name)

name = "Jackie"
print(name)


name = input("What is your name?")
length = len(name)
print(length)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Day 1 Project Code:

#1. Create a greeting for your program.
print("Welcome to the Brand Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?  \n")
#3. Ask the user for the name of a pet.
pet_name = input("What's your pet's name?  \n")
#4. Combine the name of their city and pet and show them their band name.
print("Your new name could be " + pet_name + " " + city )
#5. Make sure the input cursor shows on a new line:

