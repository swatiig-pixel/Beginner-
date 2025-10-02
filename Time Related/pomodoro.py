from tkinter import *
import time
import math
  

reps =0
timer = None

def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text,text="00:00")
  heading.config(text="Timer")
  check_mark.config(text="")
  global reps
  reps = 0


def start_timer():
  global reps
  reps += 1

  work =1 *60
  brk = 5 *60
  long_brk = 20*60

  if reps % 8 == 0:
    countdown(long_brk)
    heading.config(text="Long Break",fg="red")
  elif reps % 2 == 0:
    countdown(brk)
    heading.config(text="Break",fg="pink")
  else:
    countdown(work)
    heading.config(text="Work",fg="green")

def countdown(count):
  minutes = math.floor(count/60)
  seconds = count%60
  if seconds < 10:
    seconds = f"0{seconds}"
  if minutes < 10:
    minutes = f"0{minutes}"
  canvas.itemconfigure(timer_text,text=f"{minutes}:{seconds}")
  if count> 0:
    global timer
    timer = window.after(1000,countdown,count-1)
  else:
    start_timer()
    mark = ""
    for _ in range(math.floor(reps/2)):
      mark += "🧰"
    check_mark.config(text=mark)

window = Tk()
window.config(padx=40,pady=40,bg="#FDEBD0")



#Lable
heading = Label(text="Timer",font=("Comicsans",25,"bold"),bg="#FDEBD0")
heading.grid(column=1,row=0)


#image

canvas = Canvas(window,width=200,height=215,bg="#FDEBD0",highlightthickness=0)
canvas.grid(column=1,row=1)
image_ = PhotoImage(file="C:/Users/Swati/Downloads/pomodoro-start/tomato.png")
canvas.create_image(100,100,image=image_)
timer_text = canvas.create_text(100,120,text="00:00",fill="white",font=("Comicsans",30,"bold"))



#Start Button
start = Button(text="start",bg="#FDEBD0",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)



#reset Button
reset = Button(text="Reset",bg="#FDEBD0",highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)


#Checkmarks 
check_mark = Label(text="",bg="#FDEBD0",highlightthickness=0)
check_mark.grid(column=1,row=2)



window.mainloop()