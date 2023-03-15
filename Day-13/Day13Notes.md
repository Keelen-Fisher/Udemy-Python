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

### Step 2: Reproduce the code

- Sometimes, you have code that works for only certain conditions, like a imported random type of code for example. You can run it for a multiple amount of times and it will produce a result, and then it suddenly gives you an error. When this happens, the goal is to reproduce the code to find the exact moment and reason why it happens.

- Example:

                from random import randint
                dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
                dice_num = randint(1, 6)
                print(dice_imgs[dice_num])

- After running the code multiple times, an error shows as: **IndexError: list index is out of range**

- When you first see it, try to run it again to find which number causes the problem. We see that the third line of code produces the result.

- When we change it to ***dice_num = 6***, that is when the error occurs, so there is an issue with the index of 6, this most likely means that the index of 6 does not exist.

- so if we change that line of code to ***dice_num = randint(0, 5)***, then no errors should occur.

### Step 3: "Play Computer"

- Example:

      year = int(input("What's your year of birth?"))
      if year > 1980 and year < 1994:
        print("You are a millenial.")
      elif year > 1994:
        print("You are a Gen Z.")

- This is where you play computer. mentally run through each line of code and solve the problem using different scenarios. You will find that there is no catch in the code if you enter in 1994 as your year of birth because you do not have a conditional statement/operator that checks for that integer.

- Instead, on line 4 you should put ***elif year >= 1994***.

### Step 4: Fix the errors

- Example:

            age = input("How old are you?")
            if age > 18:
            print("You can drive at age {age}.")

- There are some common errors, such as needing to indent your line of code after you've built your if conditional statement.

             age = input("How old are you?")
             if age > 18:
              print("You can drive at age {age}.")

- However that is not all. you still have to keep in mind another error, when you run this code, you will find that the code will run an error as: **TypeError: '>' not supported between instances of 'str' and 'int'.**

- This is due to the fact the code reads the first line as a string, not an integer, add in the int method on line 1:

              age = int(input("How old are you?"))
              if age > 18:
                print("You can drive at age {age}.")

- Lastly, the code will run the correct line of print statement, but it will not show the number because of the lack of the **f** in front of the quote.

                print(f"You can drive at age {age}.")

### Step 5: Print is Your Friend

- Example:

          pages = 0
          word_per_page = 0
          pages = int(input("Number of pages: "))
          word_per_page == int(input("Number of words per page: "))
          total_words = pages * word_per_page
          print(total_words)

- Let's add in some print statements!!

          pages = 0
          word_per_page = 0
          pages = int(input("Number of pages: "))
          word_per_page == int(input("Number of words per page: "))
          total_words = pages * word_per_page
          print(f"Pages = {pages}")
          print(f"word_per_page = {word_per_page}")
          print(total_words)

- using print statements can help you to narrow down the problem in a somewhat large block of code. When you run the code, you will find that the number of pages is passed through the designated variable but not with words per page, that returns 0. Now we need to focus on the words-per-page variable, and we can see that there are 2 equal signs, there only should be one:

          pages = 0
          word_per_page = 0
          pages = int(input("Number of pages: "))
          word_per_page = int(input("Number of words per page: "))
          total_words = pages * word_per_page
          print(f"Pages = {pages}")
          print(f"word_per_page = {word_per_page}")
          print(total_words)

### Step 6: Use a Debugger

- You can use different debuggers across the internet, [Python Tutor](https://pythontutor.com/visualize.html#mode=edit) is one of them.

- Break point: Tells the computer to stop what it is doing, and then examine what all the variables and all of the functions are doing.

### Final Tips

- Take a break.

- Ask a friend.

- Run your code often, do not wait until you have built a large block of code then run, because then you will find yourself in a situation where you don't know the root cause of the problem.

- Stack Overflow.
