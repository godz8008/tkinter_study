# Geometry Manager
# Tkinter에서는 위젯들을 화면에 배치하는 방식으로 3가지 방식을 사용한다.

# Pack : 위젯.pack() 메소드를 사용하여 제공한다. 불필요한 공간을 없애고 디폴트(상하)로 패킹
# Grid : 위젯들을 테이블 레이아웃에 배치하는 방식(column, row), 위젯.grid()메소드를 사용
# Place(absolute) : 위젯을 절대 좌표로 정하여 배치, 윈도우 크기 변경에 따라 위젯들이 변경되지
# 않는다. 실제 많이 사용되지 않는 방법이다. 위젯.place()메서드를 사용

import tkinter as tk 
from tkinter import ttk 

win = tk.Tk()
lbl = tk.Label(win, text="이름")
lbl.pack()

txt = tk.Entry(win)
txt.pack()

btn = tk.Button(win,text="확인")
btn.pack()

win.mainloop()