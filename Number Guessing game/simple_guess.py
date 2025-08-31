import random

print("Hey there")

def game():
    print("You need to guess number between 1 to 100")

    choice = random.randint(1,101)


    print("You will get 10 chances to guess the number")
    chance = 10
    while chance != 0:
        select = int(input("Enter your choice: "))
        if select < choice:
            chance -= 1
            print(f"You have {chance} chance left")
            print("It's too low")
        elif select > choice:
            chance -= 1
            print(f"You have {chance} chance left")
            print("It's too high")
        else:
            print("Your guess is right")
            break
    if chance == 0:
        print("You loose! you left with zero chances")


    global again
    again = input("Wanna play again : ").lower()


again= input("Do u wanna play:").lower()
while again == "yes":
    game()
else:
    print("Thank you")