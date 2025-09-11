from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.setup(width=400,height=400)
screen.bgcolor("pink")


t = Turtle("turtle")
def move_forward():
  t.forward(7)

def upadating():
    t.penup()
    t.goto(x=0,y=-170)
    t.left(90)
    screen.listen()
    screen.onkey(key="space",fun= move_forward)









screen = Screen()
screen.exitonclick()





