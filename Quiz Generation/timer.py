from tkinter import *
import time

window = Tk()

#Lable
heading = Label(text="Timer",font=("Comicsans",19,"bold"),bg="#FDEBD0")
heading.grid(column=1,row=0)


#image
window.config(padx=40,pady=40,bg="#FDEBD0")
canvas = Canvas(window,width=200,height=215,bg="#FDEBD0",highlightthickness=0)
canvas.grid(column=1,row=1)
image_ = PhotoImage(file="C:/Users/Swati/Downloads/pomodoro-start/tomato.png")
canvas.create_image(100,100,image=image_)

#Start Button
start = Button(text="start",bg="#FDEBD0",highlightthickness=0)
start.grid(column=0,row=2)

#reset Button
reset = Button(text="Reset",bg="#FDEBD0",highlightthickness=0)
reset.grid(column=2,row=2)













window.mainloop()