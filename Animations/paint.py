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
  left(5)

write("Reminder: \nClick up to turn pen upwards\nClick down to turn pen downwards\nClick up to turn pen upwards\nClick space move forward\n",font=("Comic sans",19,"normal"),align="center")



listen()
onkey(upwards(),"u")
onkey(move(),"space")




exitonclick()