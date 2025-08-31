import random

print("\n"*40)
print("Hey there")

def game():
    print("You need to guess number between 1 to 100")
    type = input("Which level you want 'easy or 'hard' : ").lower()

    choice = random.randint(1,101)

    #for easy
    if type == "easy":
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


    #for hard
    elif type == "hard":
        print("You will get 5 chances to guess the number")
        chances = 5
        while chances != 0:
            select = int(input("Enter your choice: "))
            if select < choice:
                chances -= 1
                print(f"You have {chances} chance left")
                print("It's too low")
            elif select > choice:
                chances -= 1
                print(f"You have {chances} chance left")
                print("It's too high")
            else:
                print("Your guess is right")
                break
        if chances == 0:
            print("You loose! you left with zero chances")

    #for nothing
    else:
        print("You gave wrong input")
    global again
    again = input("Wanna play again : ")


again = input("Do you wanna play : ").lower()
while again == "yes":
    game()
else:
    print("Thank you")