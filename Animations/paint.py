from turtle import *

setup(600,600)

hideturtle()

def move():
  forward(10)

def left():
  left(15)

def right():
  right(15)

def upwards():
  setheading(90)

def downwards():
  setheading(270)

def right_curve():
  forward(5)
  right(5)

def left_curve():
  forward(5)
  

listen()
onkey(key="s",fun=move())
onkey(key="space",fun=left_curve())



exitonclick()