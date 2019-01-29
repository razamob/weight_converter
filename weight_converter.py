from tkinter import *

def convert_kg():
    kg = float(e0_value.get())
    grams = kg*1000
    pounds = kg*2.20462
    ounces = kg*35.274
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


window = Tk()

kg = Label(window, text="Kg")
kg.grid(row=0, column=0)

grams = Label(window, text="Grams")
grams.grid(row=2, column=0)

pounds = Label(window, text="Pounds")
pounds.grid(row=2, column=1)

ounces = Label(window, text="Ounces")
ounces.grid(row=2, column=2)

b1 = Button(window, text="Convert", command=convert_kg)
b1.grid(row=0, column=2)

e0_value = StringVar()
e0 = Entry(window, textvariable=e0_value)
e0.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()





