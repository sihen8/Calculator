import tkinter as tk
import better_than_clincliu_calculator as calc

def makeText(str):
    text = tk.Label(text=str)
    return text

def getEquation(event):
    equation = equation_input.get()
    equation = calc.format_equation(equation)
    calc.simplify(equation)
    equation_input.delete(0, tk.END)
    equation_input.insert(0, equation)

window = tk.Tk()

makeText("Calculator").pack()
makeText("    ").pack()
makeText("Enter in a equation, no spaces").pack()

equation_input = tk.Entry(width=50)
equation_input.pack()

solve = tk.Button(height=25, width=50, text="Solve")
solve.pack()

equation = solve.bind("<Button-1>", getEquation)


window.mainloop()