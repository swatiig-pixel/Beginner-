from turtle import Turtle , Screen
from turtle__ import Player

screen = Screen()
screen.setup(600,600)
screen.bgcolor("pink")

p = Player()

screen.listen()
screen.onkey(p.space,"space")

if p.ycor() > 280:
  p.refresh()








screen.exitonclick()