from turtle import Turtle ,Screen
import random

screen = Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")

t = Turtle()
t.hideturtle()
t.write("Guess the number between 1 - 100\nChoose your level\n1.Easy\n2.Hard",font=("Arial",19,"normal"),align="center")

level = screen.textinput("Level Choosing","Easy or Hard")

choice = random.randint(1,101)

if level and level.upper() == "EASY":
  screen.clear()
  screen.bgcolor("lightblue")
  t.penup()
  t.goto(0,250)
  t.write("You will get 10 chances to guess the number",font=("Arial",19,"normal"),align="center")
  chances = 10
  while chances != 0:
    guess = screen.textinput("Guess the number","Between 1-100")
    guess = int(guess)
    if guess < choice:
      screen.clear()
      screen.bgcolor("lightblue")
      t.penup()
      t.goto(0,250)
      chances -= 1
      t.write(f"You have {chances} chances left",font=("Arial",19,"normal"),align="center")
      t.goto(0,225)
      t.write("It's too low",font=("Arial",19,"normal"),align="center")
    elif guess > choice:
      screen.clear()
      screen.bgcolor("lightblue")
      t.penup()
      t.goto(0,250)
      chances -= 1
      t.write(f"You have {chances} chances left",font=("Arial",19,"normal"),align="center")
      t.goto(0,225)
      t.write("It's too high",font=("Arial",19,"normal"),align="center")
    else:
      screen.clear()
      screen.bgcolor("lightblue")
      t.penup()
      t.write("Your guess is right!!",font=("Arial",19,"normal"),align="center")
      break

  if chances == 0:
    screen.clear()
    screen.bgcolor("black")
    t.penup()
    t.pencolor("white")
    t.write("YOU LOOSE!! YOU LEFT WITH ZERO CHANCES",font=("Arial",19,"normal"),align="center")
    t.goto(0,-30)
    t.write(f"The number is {choice}",font=("Arial",19,"normal"),align="center")




screen.exitonclick()