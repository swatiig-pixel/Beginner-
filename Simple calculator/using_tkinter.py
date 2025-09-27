from tkinter import *

window = Tk()
window.config(padx=20,pady=20)
window.title("Simple Calculator")

#Title
head = Label(text="Calculator")
head.grid(column=0,row=0,columnspan=4)

#Entry
input_ = Entry()
input_.grid(column=0,row=1,columnspan=4)

#1
one = Button(text=1)
one.grid(column=0,row=2)

#2
two = Button(text=2)
two.grid(column=1,row=2)

#3
three = Button(text=3)
three.grid(column=2,row=2)

#4
four = Button(text=4)
four.grid(column=0,row=3)

#5
five = Button(text=5)
five.grid(column=1,row=3)

#6
six = Button(text=6)
six.grid(column=2,row=3)

#7
seven = Button(text=7)
seven.grid(column=0,row=4)

#8
eight = Button(text=8)
eight.grid(column=1,row=4)

#9
nine = Button(text=9)
nine.grid(column=2,row=4)

#plus
plus = Button(text="+")
plus.grid(column=0,row=5)

#zero
zero = Button(text=0)
zero.grid(column=1,row=5)

#minus
minus = Button(text="-")
minus.grid(column=2,row=5)

#multiply
multi = Button(text="*")
multi.grid(column=3,row=2)

#Divide
divide = Button(text="/")
divide.grid(column=3,row=3)

#=
calculate = Button(text="=")
calculate.grid(column=3,row=4)

#clear
clear = Button(text="AC")
clear.grid(column=3,row=5)

window.mainloop()