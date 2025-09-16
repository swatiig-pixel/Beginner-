from turtle import Turtle
import random

class Dice(Turtle):

  def __init__(self):
    super().__init__()
    self.shape("square")
    self.shapesize(stretch_len=4,stretch_wid=4)
    self.color("pink")


class Dots(Turtle):

  def __init__(self):
    super().__init__()
    numbers = random.randint(1,7)
    for i in range(numbers):
      self.shape("circle")
      self.color("black")
      self.shapesize(stretch_len=0.5,stretch_wid=0.5)
      if numbers == 2:
        for num in range(numbers-1):
          two_num = [-5,5]
          self.goto(two_num[num-1],0)
          

        


    
