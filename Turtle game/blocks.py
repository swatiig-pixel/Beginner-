from turtle import Turtle
import random
import time

COLORS = ["red","blue","yellow","green","orange","white","purple"]
BLOCK_MOVING_DISTANCE = 5
MOVE_INCREASE = 10

class Blocks(Turtle):
  
  def __init__(self):
    self.all_blocks = []
    self.move_speed = 0.1

  def move_speeder(self):
    self.move_speed *= 0.99

  def create_blocks(self):
    random_chance = random.randint(1,6)
    if random_chance == 1:
      block = Turtle()
      block.shape("square")
      block.penup()
      block.shapesize(stretch_wid=1,stretch_len=2)
      block.color(random.choice(COLORS))
      new_y = random.randint(-250,250)
      block.goto(280,new_y)
      self.all_blocks.append(block)

  def move_blocks(self):
    for block in self.all_blocks:
      block.backward(BLOCK_MOVING_DISTANCE)

  def many_boxes(self):
    for num in range(0,100):
      self.create_blocks()
      time.sleep(0.1)



