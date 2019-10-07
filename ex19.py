# place : 절대 위치 배치 방법

import tkinter as tk 

win = tk.Tk()
win.title("파이썬 GUI - Place")
win.geometry("640x400")
win.resizable(False, False)

btn1 = tk.Button(win, text="(100,100)")
btn1.place(x=100, y=100)

btn2 = tk.Button(win, text="(100,150)")
btn2.place(x=100, y=150, width=150, height=50)

btn3 = tk.Button(win, text="(0,200)")
btn3.place(x=0, y=200, relwidth=0.5)

btn4 = tk.Button(win, text="(0,300)")
btn4.place(y=300, relx=0.5)

btn5 = tk.Button(win, text="(300,0)")
btn5.place(x=300, rely=0.2)

btn6 = tk.Button(win, text="(0,300)", bg="yellow")
btn6.place(x=0, y=300, relx=0.5)

win.mainloop()

# place Parameter
# width, height : 위젯의 너비, 위젯의 높이
# relwidth : 위젯의 너비 비율 (0~1)
# relheight : 위젯의 높이 비율 (0~1)
# anchor : nw(기본값), n, e, w, s, ne, nw, se, sw
# relx : x좌표 배치 비율 (0~1)
# rely : y좌표 배치 비율 (0~1)