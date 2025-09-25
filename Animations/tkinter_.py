from tkinter import *

window = Tk()
window.title("First Tkinter file")
window.minsize(width=600,height=600)
window.maxsize(width=900,height=900)

name = Label(text="First file")
name.pack()

def click():
  name.config(text="It's new title")

new_button = Button(text="click me",command=click)
new_button.pack()



















window.mainloop()