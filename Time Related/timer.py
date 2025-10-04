from tkinter import *
import math

stopwatch = None
total_time = 0
def total():
  global total_time
  hours = hour.get()
  minutes = minute.get()
  seconds = second.get()
  total_time = (int(hours)*60*60)+(int(minutes)*60)+(int(seconds))

def count_down():
  global total_time, stopwatch
  new_hour = total_time // 3600
  new_min = (total_time % 3600) // 60
  new_sec = total_time % 60
  timer.config(text=f"{new_hour:02d}:{new_min:02d}:{new_sec:02d}")
  if total_time > 0:
    total_time -= 1
    stopwatch = window.after(1000,count_down)

def clear_default(event):
    if event.widget.get() == "0":
        event.widget.delete(0, END)

#windows 
window = Tk()
window.title("Timer")
window.minsize(500,500)
window.config(bg="#EEE6CA",padx=50,pady=50)

#Heading
heading = Label(text="TIMER",font=("Cascadia Mono",27,"bold"),fg="#E5BEB5",bg="#EEE6CA")
heading.pack()


#Time 
timer = Label(text="00:00:00",font=("Cascadia Mono",27,"bold"),bg="#EEE6CA",fg="#896C6C")
timer.pack()

#Hour_label
hour_label = Label(text="Enter Hours",font=("Cascadia Mono",14,"bold"),bg="#EEE6CA",fg="#896C6C")
hour_label.pack()

#entry_hour
hour = Entry(font=("Cascadia Mono",13,"bold"),bg="#EEE6CA",fg="#896C6C",width=10)
hour.insert(0,"0")
hour.bind("<FocusIn>",clear_default)
hour.pack()

#Min_label
min_label = Label(text="Enter Minutes",font=("Cascadia Mono",14,"bold"),bg="#EEE6CA",fg="#896C6C")
min_label.pack()

#entry_min
minute = Entry(font=("Cascadia Mono",13,"bold"),bg="#EEE6CA",fg="#896C6C",width=10)
minute.insert(0,"0")
minute.bind("<FocusIn>",clear_default)
minute.pack()

#Hour_label
sec_label = Label(text="Enter Seconds",font=("Cascadia Mono",14,"bold"),bg="#EEE6CA",fg="#896C6C")
sec_label.pack()

#entry_sec
second = Entry(font=("Cascadia Mono",13,"bold"),bg="#EEE6CA",fg="#896C6C",width=10)
second.insert(0,"0")
second.bind("<FocusIn>",clear_default)
second.pack()

#start
start_button = Button(text="Start",font=("Cascadia Mono",13,"bold"),bg="#896C6C",fg="#EEE6CA",command=lambda:[total(),count_down()])
start_button.pack()


window.mainloop()