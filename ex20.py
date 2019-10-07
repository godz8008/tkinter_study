# grid Parameter

# row, column : 행, 열의 위치
# rowspan : 행을 합침, 기본값은 1
# columnspan : 열을 합침, 기본값은 1
# sticky : 지정된 공간 내에서 위치 조정, n, e, s, w, nw, ne, sw, se
# ipadx : 위젯에 대한 x방향 내부패딩
# ipady : 위젯에 대한 y방향 내부패딩
# padx : 위젯에 대한 x방향 외부패딩
# pady : 위젯에 대한 y방향 외부패딩

import tkinter as tk 

win = tk.Tk()
win.title("파이썬 GUI - grid")
win.geometry("640x400")
win.resizable(False, False)

btn1 = tk.Button(win, text="(0,0)")
btn2 = tk.Button(win, text="(0,1)", width=30)
btn3 = tk.Button(win, text="(0,2)")

btn4 = tk.Button(win, text="(1,0)")
btn5 = tk.Button(win, text="(1,1)")
btn6 = tk.Button(win, text="(1,3)")

btn7 = tk.Button(win, text="(2,1)")
btn8 = tk.Button(win, text="(2,2)")
btn9 = tk.Button(win, text="(2,4)")

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0, rowspan=2)
btn5.grid(row=1, column=1, columnspan=3)
btn6.grid(row=1, column=3)

btn7.grid(row=2, column=1, sticky="e")
btn8.grid(row=2, column=2)
btn9.grid(row=2, column=90)

win.mainloop()