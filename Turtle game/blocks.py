from turtle import Turtle
import random

COLORS = ["red","blue","yellow","green","orange","white","purple"]

class Blocks(Turtle):
  
  def __init__(self):
    self.all_blocks = []
    self.move_speed = 1

  def move_speeder(self):
    self.move_speed *= 0.99

  def create_blocks(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      block = Turtle()
      block.shape("square")
      block.shapesize(stretch_wid=2,stretch_len=1)
      block.penup()
      block.color(random.choice(COLORS))
      new_y = random.randint(-250,250)
      block.goto(280,new_y)
      self.all_blocks.append()




