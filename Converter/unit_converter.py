def length_converter():
  print("\nLENGTH CONVERTER")
  print("1.Centimeters to Meters")
  print("2.Meters to Kilometers")
  print("3.Kilometers to Miles")
  choice = int(input("Choose option(1/2/3): "))

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
  print("Kilograms to pounds")
  choice = int(input("Choose option (1/2): "))

  if choice == 1:
    g = float(input("Enter weight in grams: "))
    print(f"{g} g = {g/1000:.2f} kg")

  elif choice == 2:
    kg = float(input("Enter weight in Kilograms: "))
    print(f"{kg} kg = {kg*2.20462:.2f} lbs")

  else:
    print("INVALID CHOICE!!!")