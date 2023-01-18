# Day 6

## Code Blocks, Functions and While Loops

## Defining and Calling Functions

- Functions:
  - There are built in functions that has been used for the past 5 days. These require no declaration, just calling the function with something being passed within the parenthesis.

  - [Link to Other Built In Functions:](https://docs.python.org/3/library/functions.html)

- Declaring functions:
  - First step: Define the function to specify what it should do.
  - Second step: Write the lines of code (must be indented)
  - Third Step: Call the function

        - *declare the function using :"def"

          def my_function():
            print("Hello")
            print("bye")

        - *now we call the function
          my_function()

- Declaring functions using ["Reeborg's World"](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json)

- Second assignment using functions: [Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

## Indentation in Python

- The relationship is like a file to a folder.

- Click [here](https://peps.python.org/pep-0008/) for more information on Style Guides.

## While Loop

- A loop whose condition is based on wether or not the condition is true or false.

- [4th Hurdle Assignment](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json):

  - How to solve this assignment:

          def turn_around():
              turn_left()
              turn_left()

          def turn_right():
              turn_left()
              turn_left()
              turn_left()

          def circle():
              turn_left()
              turn_left()
              turn_left()
              turn_left()
          
          def hurdle():    
              move()
              turn_left()
              move()
              turn_right()
              move()
              turn_right()
              move()
              turn_left()
          
          def over_wall():
              turn_left()
              move()
              turn_right()
              move()
              turn_right()
              move()
              turn_left()
                  
          def wall_modified():
              turn_left()
              if wall_in_front():
                  turn_left()
              else:
                  move()
              while wall_on_right():
                  if wall_in_front():
                      turn_left()
                  else:
                      move()
              turn_right()
              if right_is_clear():  
                  move()
              else:
                  turn_right()
                  move()
              if not right_is_clear():
                    turn_left()
              else:
                  turn_right()
                
          # Call 6 times 
          #hurdle()
          #hurdle()
          #hurdle()
          #hurdle()
          #hurdle()
          #hurdle()

          #Using for loop
          #for step in range(6):
              #hurdle()
              

          while at_goal() != True:
              if wall_in_front():
                wall_modified()
              elif front_is_clear():
                move()

- [Link to Maze Day 6 Project](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json):

- Solution:

        def turn_around():
            turn_left()
            turn_left()

        def turn_right():
            turn_left()
            turn_left()
            turn_left()
        
        while at_goal() != True:
            if right_is_clear():
              turn_right()
              move()
            elif front_is_clear():
                move()
            else:
                turn_left()

- ***SIDE NOTE:*** There is a potential bug using this code. Due to the fact that the maze is random each time that you run the code, you may run into an issue where the robot is stuck in an infinite loop. This is something to debug and solve later, but don't forget that you have to solve it. Once you are finished with ***Day 15,*** ensure that you come back to this challenge and solve the bug.

  - Video to come back to: [Link](https://www.udemy.com/course/100-days-of-code/learn/lecture/19115662#content)

  - Challenge to come back to: [Link](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json)
