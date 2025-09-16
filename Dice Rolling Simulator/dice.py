from turtle import Turtle
import random
import time

DIE_SIZE = 120
PIP_RADIUS = 8
class Dots:

  def __init__(self,x=0,y=0,size=DIE_SIZE):
    super().__init__()
    self.x = x
    self.y = y
    self.size = size
    self.half = size/2
    self.t= Turtle(visible=False)
    self.t.penup()
    self.t.speed(0)
    self.value = 1

  def goto(self,x,y):
    self.t.penup()
    self.t.goto(x,y)
    self.t.pendown()

  def square(self):
    self.t.penup()
    self.t.goto(self.x-self.half,self.y-self.half)
    self.t.pendown()
    self.t.pensize(3)
    self.t.color("pink","lightgreen")
    self.t.fill()
    for _ in range(4):
      self.t.forward(90)
      self.t.left(90)
    self.t.end_fill()

  def positions(self):
    offset = self.size /4
    cx ,cy = self.x,self.y
    position = {
      1:[(cx,cy)],
      2:[(cx - offset,cy - offset),(cx + offset,cy+offset)],
      3:[(cx - offset,cy - offset),(cx,cy),(cx + offset,cy+offset)],
      4:[(cx - offset,cy - offset),(cx - offset,cy+offset),(cx + offset,cy - offset),(cx + offset,cy+offset)],
      5:[(cx - offset,cy - offset),(cx - offset,cy+offset),(cx + offset,cy - offset),(cx + offset,cy+offset),(cx,cy)],
      6:[(cx - offset,cy - offset),(cx - offset,cy+offset),(cx + offset,cy - offset),(cx + offset,cy+offset),(cx-offset,cy),(cx+offset,cy)]
    }
    return position[self.value]
  

  def draw_pip(self):
    d = self.t
    d.penup()
    d.color("pink")
    for (px,py) in self.positions():
      d.goto(px,py - PIP_RADIUS/2)
      d.begin_fill()
      d.pendown()
      d.circle(PIP_RADIUS)
      d.penup()
      d.end_fill()


  def shows(self):
    self.t.clear()
    self.square()
    self.draw_pip()
    self.t.penup()
    self.t.penup()
    self.t.goto(self.x,self.y-self.half-20)
    self.t.write(f"Value: {self.value}",align="center",font=("Arial",11,"normal"))

  def set_value(self,v):
    if v < 1 or v> 6:
      raise ValueError("DIE VALUE MUST BE BETWEEN 1 AND 6")
    self.value = random.randint(1,6)
    self.shows()

  def roll(self):
    self.value = random.randint(1,6)
    self.shows()

  def animate(self,spins=12,pause=0.05):
    for i in range(spins):
      self.value = random.randint(1,6)
      self.shows()
      time.sleep(pause)
    self.value = random.randint(1,6)
    self.shows()
    return self.value
    
          

        


    
