from turtle import Turtle , Screen
import turtle as tim
import random

t = Turtle()
screen = Screen()
screen.setup(600,600)
screen.bgcolor("pink")
tim.colormode(255)
t.speed("fastest")

def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_col = (r,g,b)
  return random_col

for num in range(100):
  t.circle(50)
  t.right(5)
  t.color(random_color())
  t.forward(5)




screen.exitonclick()