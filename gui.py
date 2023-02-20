from tkinter import *
from calc import *

def makeText(str):
    text = Label(window, text=str)
    return text

def getEquation(event):
    equation = equation_input.get()
    equation = format_equation(equation)
    simplify(equation)
    equation_input.delete(0, END)
    equation_input.insert(0, equation)

window = Tk()
window.title("Calculator")
window.resizable(False, False)

makeText("Calculator").pack()
makeText("    ").pack()
makeText("Enter in a equation, no spaces").pack()

equation_input = Entry(window, width=50)
equation_input.pack()

makeText(" ").pack()

solve = Button(window, height=10, width=45, text="Solve")
solve.pack()

equation = solve.bind("<Button-1>", getEquation)

window.mainloop()