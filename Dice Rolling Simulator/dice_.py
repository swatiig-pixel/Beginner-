from turtle import Turtle
import random

class Dice(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_wid=5,stretch_len=5)
    self.color("orange")
    self.goto(150,-25)


  def intro(self):
    self.penup()
    self.goto(-50,80)
    self.color("black")
    self.write(f"Press Space to\nrotate die",font=("Arial",17,"normal"),align="right")

  def head(self):
    self.penup()
    self.goto(0,150)
    self.color("black")
    self.write(f"DIE SIMULATOR",font=("Arial",20,"bold"),align="center")

  def random_num(self):
    choice = random.randint(1,6)
    self.color("black")
    self.goto(-100,-40)
    self.write(f"{choice}",align="center",font=("Arial",27,"bold"))
