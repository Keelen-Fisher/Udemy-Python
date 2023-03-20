# Display Art
from game_data import data
import random
from art import logo, vs

# Generate a random account from the game data
def random_account():
    return random.choice(data)

def form_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# check if user is correct
def checking_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(logo)
    score = 0
    game_continue = True
    account_a = random_account()
    account_b = random_account()
    # make the game repeatable
    while game_continue:
      account_a = account_b
      account_b = random_account()
      # Making account at position B become the next account at position A
      while account_a == account_b:
          account_b = random_account()
      print(f"Compare A: {form_data(account_a)}.")
      print(vs)
      print(f"Against B: {form_data(account_b)}.")

      # Ask User for a guess
      guess = input("Who has more followers? Type 'A' or 'B': ").lower()
      a_follower_count = account_a["follower_count"]
      b_follower_count = account_b["follower_count"]
      is_correct = checking_answer(guess, a_follower_count, b_follower_count)

      # clear() / this is used in replit, to clear the screen if you got the game right.
      # get the follower count of each account
      print(logo)
      # use if statement to check if user is correct
      if is_correct:
          # score keeping
          score += 1
          # give user feedback on their guess
          print(f"You're right! Current score: {score}.")
      else:
          game_continue = False
          print(f"Sorry, that's wrong. Final Score: {score}")

game()
