from turtle import Turtle ,Screen
import random

screen = Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")

t = Turtle()
t.hideturtle()
t.write("Guess the number between 1 - 100\nChoose your level\n1.Easy\n2.Hard",font=("Arial",19,"normal"),align="center")

level = screen.textinput("Level Choosing","Easy or Hard")

random_num = random.randint(1,100)

if level and level.upper() == "EASY":
  screen.clear()
  screen.bgcolor("pink")
  t.goto(0,15)
  t.write("You will be given 10 chances to guess the number",align="center",font=("Arial",19,"normal"))
  t.goto(0,-15)
  t.write("Click space to start",align="center",font=("Arial",19,"normal"))

  def to_start():
    global guess
    guess = screen.textinput("Enter Number","Between 1-100")
    

  screen.listen()
  screen.onkey(key="space",fun=to_start)

  if random_num == int(guess):
    screen.clear()
    screen.bgcolor("black")
    t.pencolor("white")
    t.write("YOU WON!!!")

  elif random_num > int(guess):
    screen.clear()
    screen.bgcolor("black")
    t.pencolor("white")
    t.write("It's too low")

  else:
    screen.clear()
    screen.bgcolor("black")
    t.pencolor("white")
    t.write("It's high")




screen.exitonclick()