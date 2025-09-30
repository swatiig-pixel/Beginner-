from tkinter import *

def button_clear():
  tasku = task.get()
  task.delete(0,END)
  if tasku != "":
    var = IntVar()
    check_box = Checkbutton(text=tasku,variable=var,onvalue=1,offvalue=0,bg="#A7E399")
    check_box.var = var
    check_box.pack()
    tasks.append(check_box)

def remove_checked():
    for t in tasks[:]:   
        if t.var.get() == 1:   
            t.destroy()        
            tasks.remove(t) 


window = Tk()
window.minsize(width=400,height=400)
window.config(bg="#476EAE",padx=20,pady=20)

#Empty list
tasks = []


#Label
heading = Label(text="To do list",font=("Comicsans",19,"normal"),fg="#F6FF99",bg="#476EAE")
heading.pack()

#Text input
task = Entry(width=50)
task.pack()

#Add Button
add = Button(text="Add",command=button_clear,bg="#48B3AF")
add.pack()

#Remove Button
remove_checked = Button(text="Remove Checked Task",command=remove_checked,bg="#48B3AF")
remove_checked.pack()



window.mainloop()