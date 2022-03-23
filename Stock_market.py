from tkinter import *
from pandas_datareader import data as web
import pandas as pd

root = Tk()

root.title("Brazilian Stocks price")
root.geometry("290x300")

L1 = Label(root, text="Stock name")
L1.grid(row=0, column=0)
e = Entry(root)
e.grid(row=0, column=1)
e.get()


L2 = Label(root, text="Start date: MM/DD/YYYY")
L2.grid(row=1, column=0)
date1 = Entry(root)
date1.grid(row=1, column=1)
date1.get()


L3 = Label(root, text="End date: MM/DD/YYYY")
L3.grid(row=2, column=0)
date2 = Entry(root)
date2.grid(row=2, column=1)
date2.get()


def myclick():
    global mylabel
    global mylabel1
    cot = web.DataReader(e.get() + ".SA", data_source='yahoo', start=date1.get(), end=date2.get())
    cot_right = pd.DataFrame(round(cot["Adj Close"], 2))
    cot_right.columns = ["Price R$"]
    cot_right = cot_right.reset_index(level=0)
    mylabel1 = Label(root, text=f" {e.get()}")
    mylabel1.grid(row=4, column=1)
    mylabel = Label(root, text=f" {cot_right.to_string(index=False)}")
    mylabel.grid(row=5, column=1)


def button_clear():
    e.delete(0, END)
    date1.delete(0, END)
    date2.delete(0, END)


def button_clear_outputs():
    mylabel.after(0, mylabel.destroy())
    mylabel1.after(0, mylabel1.destroy())


myButton = Button(root, text="Click to see the price!", pady=10, command=myclick)
myButton.grid(row=3, column=1)
button_clear = Button(root, text="Clear inputs",  padx=44, pady=10, command=button_clear)
button_clear.grid(row=3, column=0)

button_clear_outputs = Button(root, text="Clear outputs", padx=40, pady=10, command=button_clear_outputs)
button_clear_outputs.grid(row=4, column=0)
root.mainloop()