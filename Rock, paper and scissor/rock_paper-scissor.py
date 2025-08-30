import random

#Taking Input
print("Welcome to Stone,Paper and Scissor game")
print("For rock type 1 \n For Paper type 2 \n For Scissor type 3")


value = "yes"
while value == "yes":
  player = input("Enter your Choice")
  player_choice = int(player) - 1


  #for computer
  computer_choice = random.randint(0,2)

  choice = {
      0:"rock",
      1:"paper",
      2:"scissor"
  }

  print(f"Computer chose :{choice[computer_choice]}")



#for decision
  if player_choice == 0 and computer_choice == 0:
      print("Ohh! Tie")
  elif player_choice == 0 and computer_choice == 1:
      print("You loose!")
  elif player_choice == 0 and computer_choice == 2:
      print("You win!")
  elif player_choice == 1 and computer_choice == 0:
      print("you win!")
  elif player_choice == 1 and computer_choice == 1:
      print("ohh! Tie")
  elif player_choice == 1 and computer_choice == 2:
      print("You loose!")
  elif player_choice == 2 and computer_choice == 0:
      print("You loose!")
  elif player_choice == 2 and computer_choice == 1:
      print("You win!")
  elif player_choice == 2 and computer_choice == 2:
      print("Ohh! Tie")
  else:
      print("Sorry you gave a wrong input, Input must be 1,2 or 3")
  value = input("Do you want to play again(yes/no):").lower()

print("Thank you for playing")