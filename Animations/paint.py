from turtle import *

screen = Screen()
screen.setup(600,600)
t = Turtle()



def move():
  t.forward(10)

def lefti():
  t.left(15)
  

def righti():
  t.right(15)

def upwards():
  t.setheading(90)

def downwards():
  t.setheading(270)

def right_curve():
  t.forward(5)
  t.right(5)

def left_curve():
  t.forward(5)
  t.left(5)

def color_fillz():
  t.fillcolor("yellow")
  t.begin_fill()

screen.listen()
screen.onkey(move,"space")
screen.onkey(upwards,"Up")
screen.onkey(downwards,"Down")
screen.onkey(righti,"Right")
screen.onkey(lefti,"Left")
screen.onkey(right_curve,"p")
screen.onkey(left_curve,"a")
screen.onkey(color_fillz,"f")

exitonclick()