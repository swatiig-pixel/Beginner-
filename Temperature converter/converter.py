from turtle import Turtle, Screen

screen = Screen()
screen.title("Temperture Converter")
screen.bgcolor("lightblue")
screen.exitonclick()

def celsius_to_fahrenheit(f):
  return (f*9/5) + 32

def fahrenheit_to_celsius(c):
  return (c -32)*5/9
