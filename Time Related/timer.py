from tkinter import *




#windows 
window = Tk()
window.title("Timer")
window.minsize(500,500)
window.config(bg="#EEE6CA",padx=50,pady=50)

#Heading
heading = Label(text="TIMER",font=("Cascadia Mono",27,"bold"),fg="#E5BEB5",bg="#EEE6CA")
heading.pack()


#Time 
timer = Label(text="00:00",font=("Cascadia Mono",27,"bold"),bg="#EEE6CA",fg="#896C6C")
timer.pack()

#entry
minutes = Entry(font=("Cascadia Mono",13,"bold"),bg="#EEE6CA",fg="#896C6C",width=10)
minutes.pack()

#start
start_button = Button(text="Start",font=("Cascadia Mono",13,"bold"),bg="#896C6C",fg="#EEE6CA")
start_button.pack()


window.mainloop()