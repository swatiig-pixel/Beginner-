from tkinter import *

window = Tk()
window.config(padx=20,pady=20)
window.title("Simple Calculator")

def calculate_(num1,sign,num2):
  if sign == "+":
    result = float(num1) + float(num2)

  if sign == "-":
    result = float(num1) - float(num2)

  if sign == "*":
    result = float(num1) * float(num2)

  if sign == "/":
    result = float(num1) / float(num2)

  return f"{result}"





#Title
head = Label(text="Calculator",font=("comic sans",19,"bold"))
head.grid(column=0,row=0,columnspan=4)

#Entry
input_ = Entry(font=("comic sans",19,"normal"))
input_.grid(column=0,row=1,columnspan=4)

#1
one = Button(text=1,font=("comic sans",19,"normal"))
one.grid(column=0,row=2)

#2
two = Button(text=2,font=("comic sans",19,"normal"))
two.grid(column=1,row=2)

#3
three = Button(text=3,font=("comic sans",19,"normal"))
three.grid(column=2,row=2)

#4
four = Button(text=4,font=("comic sans",19,"normal"))
four.grid(column=0,row=3)

#5
five = Button(text=5,font=("comic sans",19,"normal"))
five.grid(column=1,row=3)

#6
six = Button(text=6,font=("comic sans",19,"normal"))
six.grid(column=2,row=3)

#7
seven = Button(text=7,font=("comic sans",19,"normal"))
seven.grid(column=0,row=4)

#8
eight = Button(text=8,font=("comic sans",19,"normal"))
eight.grid(column=1,row=4)

#9
nine = Button(text=9,font=("comic sans",19,"normal"))
nine.grid(column=2,row=4)

#plus
plus = Button(text="+",font=("comic sans",19,"normal"))
plus.grid(column=0,row=5)

#zero
zero = Button(text=0,font=("comic sans",19,"normal"))
zero.grid(column=1,row=5)

#minus
minus = Button(text="-",font=("comic sans",19,"normal"))
minus.grid(column=2,row=5)

#multiply
multi = Button(text="*",font=("comic sans",19,"normal"))
multi.grid(column=3,row=2)

#Divide
divide = Button(text="/",font=("comic sans",19,"normal"))
divide.grid(column=3,row=3)

#=
calculate = Button(text="=",font=("comic sans",19,"normal"))
calculate.grid(column=3,row=4)

#clear
clear = Button(text="AC",font=("comic sans",19,"normal"))
clear.grid(column=3,row=5)

window.mainloop()