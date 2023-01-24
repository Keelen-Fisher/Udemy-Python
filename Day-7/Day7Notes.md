# Day 7

## The Hangman Project

## For Day 7, the primary focus is to extend our knowledge on For and While Loops, IF/Else Statements, Lists, Strings, Range, and Modules

## Flow Chart Programming

![Alt text](../assets/Hangman%20Project%20UML.png)

## [Hangman Code Walkthrough: Challenges 1-5:](Day7.py)

### For loops with list

- [How to use a for loop using list:](https://developers.google.com/edu/python/lists#for-and-in)

### An extended preview on Lists

- List literals are written within square brackets [ ]. Lists work similarly to strings -- use the len() function and square brackets [ ] to access data, with the first element at index 0.

        colors = ['red', 'blue', 'green']
        print(colors[0])    ## red
        print(colors[2])    ## green
        print(len(colors))  ## 3

#### List Methods

- list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
- list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
- list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
- list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
- list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
- list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
- list.reverse() -- reverses the list in place (does not return it)
- list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

### Using "in" inside of a line of code

- The *in* construct on its own is an easy way to test if an element appears in a list (or other collection) -- value in collection -- tests if the value is in the collection, returning True/False.

          list = ['larry', 'curly', 'moe']
          if 'curly' in list:
            print('yay')

### An extended preview on Range

- The range(n) function yields the numbers 0, 1, ... n-1, and range(a, b) returns a, a+1, ... b-1 -- up to but not including the last number. The combination of the for-loop and the range() function allow you to build a traditional numeric for loop:

            ## print the numbers from 0 through 99
                for i in range(100):
                  print(i)

