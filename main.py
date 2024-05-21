import tkinter as tk
from tkinter import messagebox
import math

def kill(root):
    root.destroy()

def button_click(sym):
    curr = entry_variable.get()
    entry_variable.set(curr+sym)

def clear():
    entry_variable.set("")

def calc():
    try:
        res = eval(entry_variable.get())
        entry_variable.set(str(res))
    except:
        entry_variable.set("Error")

def sqrt():
   num = entry_variable.get()
   entry_variable.set(str(math.sqrt(float(num))))

def quad():

    def calculate():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            c = float(entry_c.get())

            discriminat = b**2 - 4*a*c

            if discriminat > 0:
                root1=(-b+math.sqrt(discriminat))/ (2*a)
                root2=(-b-math.sqrt(discriminat))/ (2*a)
                result_label.config(text=f"Roots are {root1:.2f} and {root2:.2f}")
            elif discriminat == 0:
                root = -b / (2*a)
                result_label.config(text=f"Root is {root:.2f}")
            else:
                result_label.config(text="No real roots")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")
    win = tk.Tk()
    win.title("Quadratic Calculator")

    tk.Label(win, text='enter coeficents for aX^2 + bX + c = 0').grid(row=0,columnspan=2)

    tk.Label(win, text="a:").grid(row=1,column=0)
    entry_a = tk.Entry(win)
    entry_a.grid(row=1,column=1)

    tk.Label(win, text="b:").grid(row=2, column=0)
    entry_b = tk.Entry(win)
    entry_b.grid(row=2, column=1)

    tk.Label(win, text="c:").grid(row=3, column=0)
    entry_c = tk.Entry(win)
    entry_c.grid(row=3, column=1)

    calculate_button = tk.Button(win, text="Calculate Roots", command=calculate)
    calculate_button.grid(row=4, columnspan=2)

    result_label = tk.Label(win, text="Roots will be displayed here")
    result_label.grid(row=5, columnspan=2)

    killBtn = tk.Button(win, text='🚫', command=lambda:kill(win), font=("Arial", 15))
    killBtn.grid(row=6,column=0)



    win.mainloop()





root = tk.Tk()
root.title("Calculator")
entry_variable = tk.StringVar()
entry = tk.Entry(root, font=("Arial", 15), textvariable=entry_variable)
entry.grid(row=0, column=0, columnspan=4, sticky='nswe')
buttons = [
        ('7', 1, 0),('8',1,1),('9',1, 2),('/',1,3),
        ('4', 2, 0),('5',2,1),('6',2, 2),('*',2,3),
        ('1', 3, 0),('2',3,1),('3',3, 2),('-',3,3),
        ('0', 4, 0),('.',4,1),('+',4, 2),


]

for (text,row,col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 15), command=lambda symbol=text:button_click(symbol))
    button.grid(row=row,column=col, sticky='nsew')
clearBtn = tk.Button(root, text='C', font=('Arial', 15), command=clear)
clearBtn.grid(row=5, column=0, sticky='nswe')
calcBtn = tk.Button(root, text='=', font=('Arial', 15), command=calc)
calcBtn.grid(row=5, column=1, sticky='nswe')
quadBtn = tk.Button(root, text='Q', font=('Arial', 15), command=quad)
quadBtn.grid(row=5, column=2, sticky='nswe')
sqrtBtn = tk.Button(root, text='S', font=('Arial', 15), command=sqrt)
sqrtBtn.grid(row=4, column=3, sticky='nswe')
killBtn = tk.Button(root, text='🚫', font=("Arial", 15), command=lambda:kill(root))
killBtn.grid(row=5,column=3,sticky='nswe')

root.mainloop()

