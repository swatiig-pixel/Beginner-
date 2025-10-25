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
window.config(bg="#FFF1CB")
window.title("Encode and Decode")

#label
heading = Label(window,text="Encode and Decode your words!!",bg="#FFF1CB",fg="#FF8F8F",font=("Open Sans",24,"bold"))
heading.pack(anchor="center",padx=20,pady=20)

#textput
text_in = Entry(window,width=36,bg="#C2E2FA",fg="#FF8F8F",font=("Open Sans",14,"bold"))
text_in.insert(0,"Enter word ")
text_in.pack(anchor="center",padx=20,pady=20)

num_skipped = Entry(window,bg="#C2E2FA",fg="#FF8F8F",font=("Open Sans",14,"bold"))
num_skipped.insert(0,"2")
num_skipped.pack(padx=20,pady=20)

#
encode = Button(window,text="Encode",command=encode,bg="#C2E2FA",fg="#FF8F8F",font=("Open Sans",15,"bold"))
encode.pack(padx=20,pady=20)

decode = Button(window,text="Decode",command=decode,bg="#C2E2FA",fg="#FF8F8F",font=("Open Sans",15,"bold"))
decode.pack(padx=20,pady=20)


window.mainloop()