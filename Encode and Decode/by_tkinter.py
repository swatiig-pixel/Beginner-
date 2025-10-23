from tkinter import *

window = Tk()
window.minsize(width=600,height=600)
window.title("Encode and Decode")

#label
heading = Label(window,text="Encode and Decode your words!!")
heading.pack(anchor="center")

#textput
text_in = Entry(window)
text_in.pack(anchor="center")

num_skipped = Entry(window)
num_skipped.pack()

#
encode = Button(window,text="Encode")
encode.pack()

decode = Button(window,text="Decode")
decode.pack()


window.mainloop()