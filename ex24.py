# 메뉴버튼 사용

# tkinter.Menubutton(윈도우창, ....)클래스를 이용해서 메뉴버튼의 속성을 설정한 후
# 다음으로 Menu클래스를 이용해서 메뉴의 속성을 설정한다.

# 위와 같이 메뉴버튼(Menubutton)과 메뉴(Menu)를 만들었으면 서로 연결을 시켜준다.

# Menubutton Parameter

# text : 메뉴버튼에 표시할 문자열
# textvariable : 메뉴버튼에 표시할 문자열을 가져올 변수
# anchor, justify
# wraplength : 자동 줄바꿈 너비 설정

import tkinter as tk 

win = tk.Tk()
win.title("파이썬 GUI - Menubutton")
win.geometry("600x400")
win.resizable(False, False)

# direction 파라미터 : above, below(기본값), left, right, flush
menubutton = tk.Menubutton(win, text="메뉴 버튼", relief="raised", direction="right")
menubutton.pack(side="left", padx=100)

menu = tk.Menu(menubutton, tearoff=0)
# menu.add_command(label="서버메뉴1")
# menu.add_command(label="서버메뉴2")
# menu.add_command(label="서버메뉴3")
chkVar1 = tk.IntVar()
chkVar2 = tk.IntVar()
menu.add_checkbutton(label="체크 1", variable=chkVar1)
menu.add_checkbutton(label="체크 2", variable=chkVar2)


menubutton["menu"] = menu

win.mainloop()