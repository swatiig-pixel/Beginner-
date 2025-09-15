from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,380)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def new_position(self):
        self.setheading(random.randint(200,300))
        #self.forward(20)

    def move(self):
        self.new_position()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.x_move *= -1 

    def opp(self):
        self.x_move *= -1.1
        self.y_move *= -1.1
        self.move_speed *= 0.8


    def top_bounce(self):
        self.x_move *= 1
        self.y_move *= -1

    def refresh(self):
        self.goto(random.randint(-280,280),380)
        self.move_speed = 0.1
