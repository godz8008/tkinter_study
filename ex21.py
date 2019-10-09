import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.title("파이썬 GUI - LabelFarame")
win.geometry("640x400")
win.resizable(0,0)

lbFrame = ttk.LabelFrame(win, text="라벨 프레임")
lbFrame.grid(row=0, column=0, padx=10, pady=20, ipadx=20, ipady=20)

ttk.Label(lbFrame, text="Label1").grid(row=0, column=0, sticky="w")
ttk.Label(lbFrame, text="Label2").grid(row=1, column=0, sticky="w")
ttk.Label(lbFrame, text="Label3").grid(row=2, column=0, sticky="w")

win.mainloop()