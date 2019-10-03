import tkinter as tk

# tkinter 패키지의 서버모듈 ttk를 가져온다.
# ttk(themed tk를 의미) : 개선된 GUI를 제공하기 위한 모듈
from tkinter import ttk

win = tk.Tk()

win.title("Python GUI")

lb1=ttk.Label(win, text="라벨")
lb1.grid(column=0,row=0)

def clickMe():
    lb1.configure(text="버튼이 클릭되었습니다")
    btn1.configure(text="***")
    lb1.configure(foreground="blue", background="yellow")

btn1 = ttk.Button(win, text="클릭", command=clickMe)
btn1.grid(column=1,row=0)

# 기존에 사용하던 위젯 추가방식
#lb1 = tk.Label(win, text="라벨")
#lb1.pack()

#btn1 = tk.Button(win, text="클릭")
#btn1.pack()

# 화면에 GUI를 출력
win.mainloop()

# tkinter패키지는 위젯이 없는 경우 기본 크기를 사용한다.
# 그런데, 위젯을 추가하면 일반적으로 위젯을 표시하는데 필요한 만큼의 작은
# 공간을 사용하도록 최적화가 발생한다.