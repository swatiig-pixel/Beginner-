from turtle import Turtle , Screen
from dice_ import Dice

screen = Screen()
screen.setup(600,400)
screen.bgcolor("lightgreen")
screen.tracer(0)

dice = Dice()
screen.update()

head = dice.head()
intro = dice.intro()
random_num = dice.random_num()

screen.listen()
screen.onkey(dice.refresh,key="space")

dot = dice.dot()






screen.exitonclick()

