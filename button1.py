from tkinter import *

window = Tk()

b1 = Button(window, text="kojihun")
b2 = Button(window, text="60162093")
b3 = Button(window, text="hello")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=0)

window.mainloop()