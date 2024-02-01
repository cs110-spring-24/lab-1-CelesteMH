import random

puter = random.randint(1,3)
user = input("Rock, Paper, or Scissors? ")

if puter == 1:
  if user == "Rock":
    print("Tie! you both chose rock")
  elif user == "Scissors":
    print("Computer chose Rock... You Lost :(")
  elif user == "Paper":
    print("You Won! Computer chose Rock")
  else:
    print("try running her again.. check capitalization please...")
elif puter == 2:
  if user == "Scissors":
    print("Tie! you both chose scissors")
  elif user == "Rock":
    print("Computer chose Scissors... You Lost :(")
  elif user == "Paper":
    print("You Won! Computer chose Scissors")
  else:
    print("try running her again.. check capitalization please...")
elif puter == 3:
  if user == "Paper":
    print("Tie! you both chose Paper")
  elif user == "Rock":
    print("Computer chose Paper... You Lost :(")
  elif user == "Scissors":
    print("You Won! Computer chose Paper")
  else:
    print("try running her again.. check capitalization please...")
