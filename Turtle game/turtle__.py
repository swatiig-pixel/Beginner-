from turtle import Turtle,Screen

STARTING_POINT = (0,-280)
MOVE = 10
FINISHING_POINT = 280

class Player(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.setheading(90)
    self.penup()
    self.goto(0,-280)
    self.color("black")

  def space(self):
    self.forward(MOVE)

  def refresh(self):
    self.goto(STARTING_POINT)

  





