from turtle import Turtle, Screen
import turtle

screen = Screen()
screen.title("Temperture Converter")
screen.bgcolor("lightblue")



def length_converter(choice):


  if choice == 1:
    cm = float(input("Enter length in cm: "))
    print(f"{cm} cm = {cm/100:2f}m")

  elif choice == 2:
    m = float(input("Enter lenght in meters: "))
    print(f"{m} m = {m/1000:.2f} km")

  elif choice == 3:
    km = float(input("Enter length in kilometer: "))
    print(f"{km} km = {km*0.621371:.2f} miles")

  else:
    print("INVALID CHOICE!!!!")


def weight_converter():
  print("\nWEIGHT CONVERTER")
  print("1.Grams to Kilograms")
  print("2.Kilograms to pounds")
  choice = int(input("Choose option (1/2): "))

  if choice == 1:
    g = float(input("Enter weight in grams: "))
    print(f"{g} g = {g/1000:.2f} kg")

  elif choice == 2:
    kg = float(input("Enter weight in Kilograms: "))
    print(f"{kg} kg = {kg*2.20462:.2f} lbs")

  else:
    print("INVALID CHOICE!!!")


user_choice = screen.textinput("Choose Conversion","Type 'A' Length Converter\nType 'B' Weight Converter")

if user_choice and user_choice.upper() == "A":
  t = turtle.Turtle()
  t.hideturtle()
  t.penup()
  t.goto(-100,20)
  t.pendown()
  t.color("darkblue")
  t.write("\nLENGTH CONVERTER\n1.Centimeters to Meters\n2.Meters to Kilometers\n3.Kilometers to Miles")
  lenght_choice = screen.textinput("Enter your Choice(1/2/3):")
  length_converter(lenght_choice)
  screen.exitonclick()


elif user_choice and user_choice.upper() == "B":

  weight_converter()

else:
  print("INVALID CHOICE!!!!")
  