import tkinter as tk
from tkinter import ttk

# 윈도우 인스턴스 생성
win = tk.Tk()

win.title("파이썬 GUI 프로그래밍")

lb1 = ttk.Label(win, text="아이디")
lb1.grid(column=0, row=0)

def clickMe():
    lb2.configure(text= "하이! " + id.get())
    btn1.configure(state='disabled')
    id.set("더이상 입력불가")

id = tk.StringVar()
entry1 = ttk.Entry(win, textvariable = id)
entry1.grid(column=1, row=0)

btn1 = ttk.Button(win, text="클릭", command=clickMe)
btn1.grid(column=2, row=0)

lb2 = ttk.Label(win, text="")
lb2.grid(column=1, row=1)

entry1.focus()  # 포커스 설정하기

win.mainloop()