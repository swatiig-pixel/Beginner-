from turtle import Turtle , Screen
from turtle__ import Player
from blocks import Blocks
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("pink")
screen.tracer(0)

p = Player()
b = Blocks()


screen.listen()
screen.onkey(p.space,"space")

game_on = True
while game_on:
  time.sleep(b.move_speed)
  screen.update()
  b.create_blocks()
  b.move_blocks()

  for block in b.all_blocks:
    if block.distance(p) < 20:
      game_on = False

  if p.ycor()> 280:
    p.refresh()
    for block in b.all_blocks:
      b.move_speeder()







screen.exitonclick()