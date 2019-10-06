import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()

win.title("파이썬 GUI - Text/ScrolledText")

colors = ["Blue", "Yellow", "Red"]
def selColor():
    rdSel = rdColor.get()
    if rdSel == 0: win.configure(background = "Blue")
    if rdSel == 1: win.configure(background = "Yellow")
    if rdSel == 2: win.configure(background = "Red")


rdColor = tk.IntVar()
for col in range(3):
    rad = tk.Radiobutton(win, text=colors[col], variable = rdColor, value=col, command=selColor)
    rad.grid(column=col, row=0, sticky="w")

# rad1 = tk.Radiobutton(win, text="blue", variable=rdColor, value=0, command=selColor)
# rad1.grid(column=0, row=0)

# rad2 = tk.Radiobutton(win, text="Yellow", variable=rdColor, value=1, command=selColor)
# rad2.grid(column=1, row=0)

# rad3 = tk.Radiobutton(win, text="Red", variable=rdColor, value=2, command=selColor)
# rad3.grid(column=2, row=0)

# txtCooments = tk.Text(win)
# txtCooments.grid(column=0, row=0)

txtComments = scrolledtext.ScrolledText(win, width=30, height=3, wrap='word')
txtComments.grid(column=0, columnspan=3)

win.mainloop()