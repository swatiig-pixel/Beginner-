from turtle import Turtle 

class Brick(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_len=3,stretch_wid=1)
    self.color("white")
    self.goto(0,-380)


  def left_move(self):
    self.backward(25)

  def right_move(self):
    self.forward(25)
    self.move_speed = 1

