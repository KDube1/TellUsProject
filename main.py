from tkinter import *

window = Tk()

window.title("ConUHacks")

lbl = Label(window, text="Hello", font=("Helvetica", 50))

lbl.grid(column=0, row=2)

window.geometry('800x500')

btn = Button(window, text="Click Me")

btn.grid(column=0, row=1)

window.mainloop()