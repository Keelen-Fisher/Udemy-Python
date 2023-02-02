# Day 9

## Dictionaries and Nesting

### [Silent Auction Program](auction.py)

### [Day 9 Code](Day9.py)

### Dictionaries

- Works similarly as dictionaries in real life. Can be visualized as a table. Dictionaries allows us to store data in values in key:value pairs. Good to use whenever you want to find a certain Python object.

  - Syntax example: {Key: Value}

  - You can add more than one entry

    - Example:

        {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

- When using dictionary, if you type in the wrong key, it will result in a return of KeyError in the terminal.

### Nesting

- Nested (or inner, nested) functions are functions that we define inside other functions to directly access the variables and names defined in the enclosing function. Nested functions have many uses, primarily for creating closures and decorators.

- A nested dictionary is a dictionary inside a dictionary/list/other-structure. It's a collection of dictionaries into one single dictionary.

- Example:

          {
            Key1: [List],
            key2: {Dict},
            Key3: Value3,
          }

- Example of a code error using dictionary:

          dict = {
              "a": 1,
              "b": 2,
              "c": 3,
          }

  - print(dict[1]) will produce an error because there is no key that matches 1, this will give you a KeyError. Unlike with a Python List, using the [1] square bracket notation on a dictionary will *not* retrieve the second item.

- Example of finding a specific "item":

        order = {
        "starter": {1: "Salad", 2: "Soup"},
        "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
        "dessert": {1: ["Ice Cream"], 2: []},
        }

  - to print "Steak", you will use print(order["main"][2][0]). [2] accesses the value with key 2, [0] gets the first item from the list.

- Auction Flow Chart

- ![Alt text](../assets/Auction%20Flow%20Chart.png)
