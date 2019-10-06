import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
win.geometry("400x400")

# label = ttk.Label(win, text = "Hello!")
# label.pack()

label = ttk.Label(win, text = "파이썬 파이썬\n파이썬",justify=tk.RIGHT
                              , background="yellow",width=20, relief="solid", anchor=tk.N)
label.pack()

# label.config(text = "Hello python")
# label.config(wraplength=130)
# label.config(background = "yellow")

win.mainloop()
    
# Frame 위젯 : Labelframe, RadioButton, CheckButtonFrame