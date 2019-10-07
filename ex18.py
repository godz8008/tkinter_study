# pack : place가 절대 위치 방법이라면, 상대위치 배치방법이다.

# pack Parameter

# side : top(기본값), bottom, left, right
# anchor : center(기본값), n, e, s, w, ne, nw, se, sw
# fill : none(기본값), x, y, both
# expand : False(기본값), True
# padx : 위젯에 대한 x방향으로 외부패딩
# pady : 위젯에 대한 y방향으로 외부패딩
# ipadx : 위젯에 대한 x방향으로 내부 패딩
# ipady : 위젯에 대한 y방향으로 내부 패딩

# pack()은 grid()와는 같이 사용할 수 없다. 하지만 place와는 같이 사용 가능하다.

import tkinter as tk 

win =tk.Tk()
win.title("파이썬 GUI - Pack")
win.geometry("640x400")
win.resizable(0, 0)

btn1 = tk.Button(win, text = "top")
btn1_1 = tk.Button(win, text = "top-1")

btn2 = tk.Button(win, text="bottom")
btn2_1 = tk.Button(win, text="bootom2")

btn3 = tk.Button(win, text="left")
btn3_1 = tk.Button(win, text="left2")

btn4 = tk.Button(win, text="right")
btn4_1 = tk.Button(win, text="right2")

btn5 = tk.Button(win, text="center", bg="yellow")

btn1.pack(side="top")
btn1_1.pack(side="top", fill="x")

btn2.pack(side="bottom")
btn2_1.pack(side="bottom", anchor="e")

btn3.pack(side="left")
btn3_1.pack(side="left", fill="y")

btn4.pack(side="right")
btn4_1.pack(side="right", anchor="s")

btn5.pack(fill="both", expand=True)

win.mainloop()