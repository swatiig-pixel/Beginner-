from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.title("Unit Converter")
screen.bgcolor("lightgreen")

result = 0


def length_converter(choice):
  global result


  if choice == 1:
    cm = float(screen.textinput("lenght","Enter length in cm: "))
    result = f"{cm} cm = {cm/100:2f}m"

  elif choice == 2:
    m = float(screen.textinput("Length","Enter lenght in meters: "))
    result = f"{m} m = {m/1000:.2f} km"

  elif choice == 3:
    km = float(screen.textinput("Length","Enter length in kilometer: "))
    result = f"{km} km = {km*0.621371:.2f} miles"

  else:
    result = "INVALID CHOICE!!!!"


def weight_converter(choice):
  global result

  if choice == 1:
    g = float(screen.textinput("Weight","Enter weight in grams: "))
    result = f"{g} g = {g/1000:.2f} kg"

  elif choice == 2:
    kg = float(screen.textinput("Weight","Enter weight in Kilograms: "))
    result = f"{kg} kg = {kg*2.20462:.2f} lbs"

  else:
    result = "INVALID CHOICE!!!"


user_choice = screen.textinput("Choose Conversion","Type 'A' Length Converter\nType 'B' Weight Converter")

if user_choice and user_choice.upper() == "A":
  length_choice = screen.textinput("\nLENGTH CONVERTER","\n1.Centimeters to Meters\n2.Meters to Kilometers\n3.Kilometers to Miles")
  length_choice = int(length_choice)
  length_converter(length_choice)


elif user_choice and user_choice.upper() == "B":
  weight_choice = screen.textinput("\nWEIGHT CONVERTER\n","1.Grams to Kilograms\n2.Kilograms to pounds")
  weight_choice = int(weight_choice)
  weight_converter(weight_choice)

else:
  result = "INVALID CHOICE!!!!"
  

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-150,20)
t.pendown()
t.color("green")
t.write(result, font=("Arial",20,"normal"))

turtle.done()