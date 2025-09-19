from turtle import Turtle ,Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")

t = Turtle()
t.hideturtle()
t.write("Guess the number between 1 - 100\nChoose your level\n1.Easy\n2.Hard",font=("Arial",19,"normal"),align="center")

level = screen.textinput("Level Choosing","Easy or Hard")

if level and level.upper() == "EASY":
  screen.clear()
  screen.bgcolor("pink")
  t.goto(0,15)
  t.write("You will be given 10 chances to guess the number",align="center",font=("Arial",19,"normal"))
  t.goto(0,-15)
  t.write("Click space to start",align="center",font=("Arial",19,"normal"))

  def to_start():
    screen.textinput("Enter Number","Between 1-100")

  screen.listen()
  screen.onkey(key="space",fun=to_start)


screen.exitonclick()