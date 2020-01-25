from tkinter import *

window = Tk()

window.title("ConUHacks")

lbl = Label(window, text="Hello", font=("Helvetica", 50))

lbl.grid(column=0, row=0)

window.geometry('800x500')

rad1 = Radiobutton(window, text='First', value=1)

rad2 = Radiobutton(window, text='Second', value=2)

rad3 = Radiobutton(window, text='Third', value=3)

rad1.grid(column=0, row=1)

rad2.grid(column=1, row=1)

rad3.grid(column=2, row=1)

window.mainloop()