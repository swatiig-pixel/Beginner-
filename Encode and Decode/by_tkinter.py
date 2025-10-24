from tkinter import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode():
  word_to_encode = text_in.get()
  shift_amount = int(num_skipped.get())
  output_text = ""

  for letter in word_to_encode:
    if letter not in alphabet:
      output_text += letter
    else:


      shifted_position = alphabet.index(letter) + shift_amount
      shifted_position %= len(alphabet)
      output_text += alphabet[shifted_position]
  encoded_word = Label(window,text=output_text)
  encoded_word.pack()


def decode():
  word_to_encode = text_in.get()
  shift_amount = int(num_skipped.get())
  shift_amount *= -1
  output_text = ""

  for letter in word_to_encode:
    if letter not in alphabet:
      output_text += letter
    else:


      shifted_position = alphabet.index(letter) + shift_amount
      shifted_position %= len(alphabet)
      output_text += alphabet[shifted_position]
  decoded_word = Label(window,text=output_text)
  decoded_word.pack()


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
encode = Button(window,text="Encode",command=encode)
encode.pack()

decode = Button(window,text="Decode",command=decode)
decode.pack()


window.mainloop()