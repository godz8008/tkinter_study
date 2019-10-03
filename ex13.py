# Radiobutton

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("파이썬 GUI - Radiobutton")
Color1 = "Blue"
Color2 = "Yellow"
Color3 = "Red"

def sel_rbtn():
    radValue = radColor.get()
    if radValue == 1: win.configure(background=Color1)
    if radValue == 2: win.configure(background=Color2)
    if radValue == 3: win.configure(background=Color3)

radColor = tk.IntVar()

rad1 = tk.Radiobutton(win, text=Color1, value=1, variable=radColor, command=sel_rbtn)
rad1.grid(column=0, row=0, sticky='w')

rad2 = tk.Radiobutton(win, text=Color2, value=2, variable=radColor, command=sel_rbtn)
rad2.grid(column=1, row=0, sticky='w')

rad3 = tk.Radiobutton(win, text=Color3, value=3, variable=radColor, command=sel_rbtn)
rad3.grid(column=2, row=0, sticky='w')

win.mainloop()