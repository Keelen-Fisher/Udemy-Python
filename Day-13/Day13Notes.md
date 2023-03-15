# Day 13

## Debugging - How to find and fix errors in your code

### Step 1: Describe the problem

- Untangle the problem and understand where it is located.

- Example:

            def my_function():
              for i in range(1, 20):
                if i == 20:
                  print("You got it")
            my_function()

- In this code, ask yourself:

  - What is the for-loop doing?

  - When is the function meant to print "You got it"?

  - What are your assumptions about it?

  - Examine the for loop, it has a range BETWEEN 1 to 20, yet i is set equal to 20 in the if statement. It never reaches to 20 because it doesn't exist. That is the problem identified

  - Instead, it should be ***for i in range(1, 21):***

  - In your code, always try to describe it to determine whether or not a line of code is true or false.

### Step 2: 
