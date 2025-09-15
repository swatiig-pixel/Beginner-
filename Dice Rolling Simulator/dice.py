from turtle import Turtle

class Dice(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("square")
    self.shapesize(stretch_len=4,stretch_wid=4)
    self.color("pink")


class Dots(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("black")
    self.shapesize(stretch_len=0.5,stretch_wid=0.5)