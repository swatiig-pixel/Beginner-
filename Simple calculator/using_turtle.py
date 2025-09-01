from turtle import Turtle, Screen
from tkinter import *

screen = Screen()
screen.setup(width=400,height=600)
screen.bgcolor("white")
screen.title("Calculator")
t = Turtle()
t.hideturtle()
t.penup()
t.goto(-140,250)
t.pendown()
t.color("blue")
t.write("Python Calculator",font=("Arial",24,"bold"))
screen.exitonclick()



