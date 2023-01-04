# Day 4

## Randomization and Python Lists

### [Example Code from Day 4](Day4.py)

#### Randomization

- This is used when we want a certain level of unpredictability.

- Machines are ***Deterministic***, operates on 0's and 1's

- [Where to find the methods and importing tutorial for using randomization:](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)

- randint(a, b): Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.

#### Module

- When a code is long and complicated, it is important to split the code into individual ***modules***, with each module performing a different set of functionality.

#### Lists (Really, really important)

- A part of a ***Data Structure***,  

- A way of organizing and storing data in Python.

- How to build a list? Here's an example:

        fruits = [item1, item2]

- A list can store any data type, and can even have mixed data types.

- Essentially, it's similar to arrays, even by it's index.

- Example of looking for a specific piece of data in a list using a printing method with index of:

      states_of_america = ["Delaware", "Pennsylvania", "New Mexico", "Texas", "Georgia", "Connecticut", "Maryland", "South Carolina", "Virginia", "Indiana"]

        print(states_of_america[0])

        ***Delaware.***

      states_of_america = ["Delaware", "Pennsylvania", "New Mexico", "Texas", "Georgia", "Connecticut", "Maryland", "South Carolina", "Virginia", "Indiana"]

        print(states_of_america[-1])

        ***Indiana.***

- list.append(x)
  - Add an item to the end of the list. Equivalent to a[len(a):] = [x].

- For more information on what Lists can do: [Link](https://docs.python.org/3/tutorial/datastructures.html)

#### Python's Data Structure
