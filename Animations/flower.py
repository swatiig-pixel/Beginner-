from turtle import *
import random

bgcolor("black")
speed("fastest")
pencolor("white")
fillcolor("red")

colors = ["red","blue","lightblue","green","lightgreen","orange","pink","brown","white"]


n = 10
while n !=0:
  n =n- 1
  for  i in range(7):
    color("red")
    begin_fill()
    circle(100,60)
    left(120)
    circle(100,60)
    left(60)
    end_fill()
    left(10)

  goto(0,-5)
  color("yellow")
  begin_fill()
  circle(5)
  end_fill()

  hideturtle()
  penup()
  rand_x = random.randint(-400,400)
  rand_y = random.randint(-400,400)
  goto(rand_x,rand_y)














done()