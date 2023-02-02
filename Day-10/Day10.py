# Functions with Outputs 

def format_name(first_name, last_name):
  formatted_first_name = first_name.title()
  formatted_last_name = last_name.title()
  return f"{formatted_first_name} {formatted_last_name}"
  # print(f"{formatted_first_name} {formatted_last_name}")
  
formatted_string = format_name("KeElEN", "FiShER")
print(formatted_string)

# ---------------------------------------------------------------------------------------------------------------------------

# Multiple Return Values

def format_name(first_name, last_name):
  if first_name == "" or last_name == "":
    return "You did not provide valid inputs."
  formatted_first_name = first_name.title()
  formatted_last_name = last_name.title()
  return f"Result: {formatted_first_name} {formatted_last_name}"
  
  # print(f"{formatted_first_name} {formatted_last_name}")
  
formatted_string = format_name(input("What is your first name? \n"), input("What is your last name? \n"))
print(formatted_string)
# output = len("Keelen")

# ---------------------------------------------------------------------------------------------------------------------------

# Exercise 1:

# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.
# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "Invalid Month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
      return 29
  return month_days[month - 1]

# Asking the user to input a year and then converting it to an integer.
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# ---------------------------------------------------------------------------------------------------------------------------





