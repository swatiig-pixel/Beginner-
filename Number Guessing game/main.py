from turtle import Turtle ,Screen

screen = Screen()
screen.setup(600,600)
screen.bgcolor("lightblue")

t = Turtle()
t.hideturtle()
t.write("Guess the number between 1 - 100\nChoose your level\n1.Easy\n2.Hard",font=("Arial",19,"normal"),align="center")



screen.exitonclick()