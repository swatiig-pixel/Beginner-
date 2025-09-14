from turtle import Turtle ,Screen
from brick import Brick
from ball import Ball

screen = Screen()
screen.bgcolor("lightgreen")
screen.setup(600,600)
screen.update()
brick = Brick()
ball = Ball()

screen.listen()
screen.onkey(brick.left_move,"A")
screen.onkey(brick.right_move,"K")

game_on = True 


screen.exitonclick()

