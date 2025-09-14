from turtle import Turtle
import random

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.color("red")
    
  def move(self):
    self.setheading(random.randint(0,180))
    self.forward(20)