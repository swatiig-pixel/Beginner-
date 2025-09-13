from turtle import Turtle 

class Brick(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_len=2,stretch_wid=1)
    self.color("pink")
    self.goto(0,-280)


  def left_move(self):
    self.backward(5)

  def right_move(self):
    self.forward(5)