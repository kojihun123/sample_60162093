from tkinter import *

window = Tk()

b1 = Button(window, text="kojihun")
b2 = Button(window, text="60162093")
b3 = Button(window, text="hello")
b4 = Button(window, text="bye")
b5 = Button(window, text="dsfsd")
b6 = Button(window, text="abcd")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=0)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=3, column=0)

print("hi")

window.mainloop()