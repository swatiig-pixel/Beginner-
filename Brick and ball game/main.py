from turtle import Turtle ,Screen
from brick import Brick
from ball import Ball
import random

screen = Screen()
screen.bgcolor("lightgreen")
screen.setup(600,600)
screen.update()
brick = Brick()
ball = Ball()

screen.listen()
screen.onkey(brick.left_move,"A")
screen.onkey(brick.right_move,"K")

angle = ball.setheading(random.randint(0,180))

game_on = True 
while game_on:
  
  ball.forward(5)
  if ball.xcor() > 280:
    ball.bounce(num=angle)


screen.exitonclick()

