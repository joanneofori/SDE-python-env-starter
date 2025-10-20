from random import randrange
playAgain = "Yes"

while playAgain == "Yes":
  playerChoice = input("Choose: Rock, Paper, or Scissors: ")
  choices = ["Rock","Paper","Scissors"]
  computerChoice = choices[randrange(3)]
  print("The computer chose " + computerChoice)
  print("You chose " + playerChoice)
  if computerChoice == playerChoice:
    print("It's a tie!")
  elif computerChoice == "Rock":
    if playerChoice == "Paper":
      print("You win!")
    else:
      print("You Lose")
  elif computerChoice == "Paper":
    if playerChoice == "Rock":
      print ("You lose")
    else:
      print ("You win!")
  elif computerChoice == "Scissors":
    if playerChoice == "Rock":
      print("You win!")
    else:
      print("You lose")
  playAgain = input("Do you want to play again?: ")
  print("")
