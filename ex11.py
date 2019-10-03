import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

def select():
    lb2.configure(text=fruitName.get() + "을 "+ amount.get() +"개를 선택하셨습니다.")


ttk.Label(win, text = "과일명 입력: ").grid(column=0, row=0)

fruitName = tk.StringVar()
fruitEntry = ttk.Entry(win, width=15, textvariable = fruitName)
fruitEntry.grid(column=0, row=1)

btn1 = ttk.Button(win, text="확인", command=select)
btn1.grid(column=2,row=1)

ttk.Label(win, text="수량을 선택 : ").grid(column=1,row=0)

amount = tk.StringVar()
combo1 = ttk.Combobox(win, width=10, textvariable = amount)
combo1.grid(column=1, row=1)
combo1['values'] = (5,10,20,30)

lb2 = ttk.Label(win, text = "")
lb2.grid(column=0, row=2)

fruitEntry.focus()

win.mainloop()