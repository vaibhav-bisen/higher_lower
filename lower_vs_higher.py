import random
from art import logo,vs
from game_data import data
from replit import clear

# Random select data function
def random_choice_data(data):
  """Select random data from the game_data"""
  choice = random.choice(data)
  return choice
  
# Fornmate data function  
def formate_data(data_choice):
  """Formate the select data"""
  name = data_choice["name"]
  description = data_choice["description"]
  country = data_choice["country"]
  return (f"{name}, {description}, {country}")
  
# Compare follower of two account function
def compare_follower(guess,a_follower,b_follower):
  """Check whos more follower"""
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"
# Game function   
def game():
  print(logo)
  score = 0
  game_should_continue = True
  # Choose random data for both account
  account_a = random_choice_data(data)
  account_b = random_choice_data(data)
  while game_should_continue:
    account_a = account_b
    account_b = random_choice_data(data)
    
    while account_a == account_b:
      account_b = random_choice_data(data)
   
    # Formate choose data
    formate_data_a = formate_data(account_a)
    formate_data_b = formate_data(account_b)
    # Follower of the both accounts
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    
    print("Compare A: "+ formate_data_a)
    print(vs)
    print("Compare B: "+ formate_data_b)
    #print(a_follower)
    #print(b_follower)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    check = compare_follower(guess,a_follower,b_follower)
    clear()
    print(logo)
    # Check who has more follower
    if check:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      print(f"Sorry that's wrong! Current score: {score}.")
      # Game should terminate if check ins not equal to the guess
      game_should_continue = False
    
game()
