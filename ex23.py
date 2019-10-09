import tkinter as tk 

win = tk.Tk()

menuBar = tk.Menu(win)
menu1 = tk.Menu(win, tearoff=0)
submenu = tk.Menu(win, tearoff=0)
submenu.add_radiobutton(label="Option 1")
submenu.add_radiobutton(label="Option 2")

menuBar.add_cascade(label="Menu 1", menu=menu1)
menu1.add_cascade(label="Submenu", menu=submenu)

win.config(menu=menuBar)

win.mainloop()