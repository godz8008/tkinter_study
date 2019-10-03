# 체크 버튼(Check Button)

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI - Checkbutton")

# Checkbutton의 상태를 나타낼때 즉, 체크가 되지 않았을 때 0으로 표시
# 체크가 되었을 때는 1로 표시할 수 있다.

ent1 = tk.Entry(win)
ent1.grid(column=0, row=0)

ent2 = tk.Entry(win)
ent2.grid(column=1, row=0)

chk1 = tk.Checkbutton(win, text="독서", state="disabled")
chk1.select() 
chk1.grid(column=0, row=1, sticky= "EW") # sticky속성을 tk.W로하면 서쪽 정렬

chk2 = tk.Checkbutton(win, text="운동")
chk2.select()  # select()와 반대 chk2.deselect()
chk2.grid(column=1, row=1)

chk3 = tk.Checkbutton(win, text="영화감상")
chk3.grid(column=2, row=1)

win.mainloop()