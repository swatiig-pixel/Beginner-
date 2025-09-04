from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.title("Temperture Converter")
screen.bgcolor("lightblue")


def celsius_to_fahrenheit(f):
  return (f*9/5) + 32

def fahrenheit_to_celsius(c):
  return (c -32)*5/9


user_choice = screen.textinput("Choose Conversion","Type 'F' to convert into Fahrenheit\nType 'C' to convert into Celsius")

if user_choice and user_choice.upper() == "F":
  celsius = float(screen.textinput("Celsius","Type the temperature in celsius:"))
  fahrenheit = celsius_to_fahrenheit(celsius)
  result = f"{celsius}°C = {fahrenheit:.2f}°F"

elif user_choice and user_choice.upper() == "C":
  fahrenheit=float(screen.textinput("Fahrenheit","Type the temperature in Fahrenheit:"))
  celsius= fahrenheit_to_celsius(fahrenheit)
  result = f"{fahrenheit}°F = {celsius:.2f}°"

else:
  result = "INVALID CHOICE!!!"

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-100,20)
t.pendown()
t.color("darkblue")
t.write(result, font=("Arial",20,"normal"))

turtle.done()
