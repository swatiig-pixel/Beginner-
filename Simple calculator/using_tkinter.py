from tkinter import *

def button_clear():
    input_.delete(0, END)

def button_equal():
    try:
        expression = input_.get()
        result = eval(expression)
        input_.delete(0, END)
        input_.insert(0, str(result))
    except Exception:
        input_.delete(0, END)
        input_.insert(0, "Error")

def button_click(value):
    current = input_.get()
    input_.delete(0, END)
    input_.insert(0, current + str(value))



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
one = Button(text=1,font=("comic sans",19,"normal"),command=lambda:button_click(1))
one.grid(column=0,row=2)

#2
two = Button(text=2,font=("comic sans",19,"normal"),command=lambda:button_click(2))
two.grid(column=1,row=2)

#3
three = Button(text=3,font=("comic sans",19,"normal"),command=lambda:button_click(3))
three.grid(column=2,row=2)

#4
four = Button(text=4,font=("comic sans",19,"normal"),command=lambda:button_click(4))
four.grid(column=0,row=3)

#5
five = Button(text=5,font=("comic sans",19,"normal"),command=lambda:button_click(5))
five.grid(column=1,row=3)

#6
six = Button(text=6,font=("comic sans",19,"normal"),command=lambda:button_click(6))
six.grid(column=2,row=3)

#7
seven = Button(text=7,font=("comic sans",19,"normal"),command=lambda:button_click(7))
seven.grid(column=0,row=4)

#8
eight = Button(text=8,font=("comic sans",19,"normal"),command=lambda:button_click(8))
eight.grid(column=1,row=4)

#9
nine = Button(text=9,font=("comic sans",19,"normal"),command=lambda:button_click(9))
nine.grid(column=2,row=4)

#plus
plus = Button(text="+",font=("comic sans",19,"normal"),command=lambda:button_click("+"))
plus.grid(column=0,row=5)

#zero
zero = Button(text=0,font=("comic sans",19,"normal"),command=lambda:button_click(0))
zero.grid(column=1,row=5)

#minus
minus = Button(text="-",font=("comic sans",19,"normal"),command=lambda:button_click("-"))
minus.grid(column=2,row=5)

#multiply
multi = Button(text="*",font=("comic sans",19,"normal"),command=lambda:button_click("*"))
multi.grid(column=3,row=2)

#Divide
divide = Button(text="/",font=("comic sans",19,"normal"),command=lambda:button_click("/"))
divide.grid(column=3,row=3)

#=
calculate = Button(text="=",font=("comic sans",19,"normal"),command=button_equal)
calculate.grid(column=3,row=4)

#clear
clear = Button(text="AC",font=("comic sans",19,"normal"),command=button_clear)
clear.grid(column=3,row=5)

window.mainloop()