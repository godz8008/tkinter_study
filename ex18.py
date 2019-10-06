# pack : place가 절대 위치 배치방법이라면, 상대위치 배치방법이다.

# pack Parameter

# side : top(기본값), bottom, left, right
# anchor : center(기본값), n, e, s, w, ne, nw, se, sw
# fill : none(기본값), x, y, both
# expand : False(기본값), True
# padx : 웨젯에 대한 x방향으로 외부패딩
# pady : 웨젯에 대한 y방향으로 외부패딩
# ipadx : 위젯에 대한 x방향으로 내부패딩
# ipady : 위젯에 대한 y방향으로 내부패딩

# pack()은 grid()와는 같이 사용할 수 없다. 하지만 palce와는 같이 사용 가능하다.

import tkinter as tk 

win = tk.Tk()
win.title("파이썬 GUI - pack")
win.resizable(0, 0)

btn1 = tk.Button(win, text = "top")
btn1_1 = tk.Button(win, text = "top-1")

btn1.pack(side="top")
btn1_1.pack(side="top", fill="x")

win.mainloop()