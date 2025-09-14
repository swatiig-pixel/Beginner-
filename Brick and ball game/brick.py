from turtle import Turtle 

class Brick(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_len=3,stretch_wid=1)
    self.color("black")
    self.goto(0,-280)


  def left_move(self):
    self.backward(10)

  def right_move(self):
    self.forward(10)

  def bounce(self):
    self.setheading(0)
    self.forward(10)