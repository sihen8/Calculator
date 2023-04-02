from tkinter import *
from calc import *

root = Tk()
root.title("Simple Calculator")

"# Display area"

e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=5, padx=12, pady=12)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_dot():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str("."))


def button_clear():
    e.delete(0, END)


def button_add():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str("+"))

def button_minus():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str("-"))


def button_multiply():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str("*"))


def button_divide():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str("/"))


def button_equals():
    expression = e.get()
    expression = solve_this(expression)
    e.delete(0, END)
    e.insert(0, expression)


"# Making the number buttons"

button_1 = Button(root, text="1", command=lambda: button_click(1), padx=30, pady=20).grid(row=3, column=0)
button_2 = Button(root, text="2", command=lambda: button_click(2), padx=30, pady=20).grid(row=3, column=1)
button_3 = Button(root, text="3", command=lambda: button_click(3), padx=30, pady=20).grid(row=3, column=2)

button_4 = Button(root, text="4", command=lambda: button_click(4), padx=30, pady=20).grid(row=2, column=0)
button_5 = Button(root, text="5", command=lambda: button_click(5), padx=30, pady=20).grid(row=2, column=1)
button_6 = Button(root, text="6", command=lambda: button_click(6), padx=30, pady=20).grid(row=2, column=2)

button_7 = Button(root, text="7", command=lambda: button_click(7), padx=30, pady=20).grid(row=1, column=0)
button_8 = Button(root, text="8", command=lambda: button_click(8), padx=30, pady=20).grid(row=1, column=1)
button_9 = Button(root, text="9", command=lambda: button_click(9), padx=30, pady=20).grid(row=1, column=2)

button_0 = Button(root, text="0", command=lambda: button_click(0), padx=30, pady=20).grid(row=4, column=0)

"# Making the special buttons"

button_clear = Button(root, text="C", command=button_clear, padx=40, pady=20).grid(row=1, column=3, columnspan=2)
button_add = Button(root, text="+", command=button_add, padx=17, pady=20).grid(row=2, column=3)
button_minus = Button(root, text="-", command=button_minus, padx=16, pady=20).grid(row=2, column=4)
button_multiply = Button(root, text="x", command=button_multiply, padx=18, pady=20).grid(row=3, column=3)
button_divide = Button(root, text="/", command=button_divide, padx=16, pady=20).grid(row=3, column=4)
button_equals = Button(root, text="=", command=button_equals, padx=78, pady=20).grid(row=4, column=2, columnspan=3)
button_dot = Button(root, text=".", command=button_dot, padx=31, pady=20).grid(row=4, column=1)

root.mainloop()