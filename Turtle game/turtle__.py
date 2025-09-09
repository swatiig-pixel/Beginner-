from turtle import Turtle, Screen
import turtle
import random

screen = Screen()
screen.setup(width=400,height=400)
screen.bgcolor("pink")

t = turtle()
t.shape("turtle")

timmy_the_turtle = t.Turtle()

colours = ["black","blue","pink","red","yellow","green","orange","purple","brown","wheat"]

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rand_color = (r,g,b)
    return rand_color



degre = [90,180,0,270]

for walk in range(200):
    degree = random.choice(degre)
    timmy_the_turtle.right(degree)
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.forward(15)
    timmy_the_turtle.speed(2400)
    timmy_the_turtle.width(5)





screen = Screen()
screen.exitonclick()





