# Menu 만들기

# 메뉴 이름 = tk.Menu(윈도우창): 해당 윈도우 창에 메뉴를 사용할 수 있다.
# 윈도우 창.config(menu=메뉴이름) : 해당 윈도우 창에 메뉴를 등록

# Menu 메소드
# add_command(인수) : 기본메뉴 항목 생성
# add_radiobutton(인수) : 라디오버튼 메뉴 항목 생성
# add_checkbutton(인수) : 체크번튼 메뉴 항목 생성
# add_cascade(인수) : 상위메뉴와 하위 메뉴를 연결
# add_separator() : 구분선 생성
# add(유형, 인수) : 특정유형의 메뉴항목 생성
# delete(start_index, end_index) : start_index에서  end_index까지 메뉴항목 삭제
# entryconfig(index, 인수) : index위치의 메뉴 항목 수정
# index(item) : item메뉴항목의 index위치를 반환
# insert_separator(index) = index위치에 구분선생성
# invoke(index) : index 위치의 항목 실행
# type(속성) 

import tkinter as tk 

win=tk.Tk()
win.title("파이썬 GUI - menu")
win.geometry("600x400")
win.resizable(0,0)

menu_bar = tk.Menu(win)

def _quit():
    win.quit()

win.config(menu = menu_bar)

file_menu = tk.Menu(menu_bar)
file_menu.add_command(label="서버메뉴1")
file_menu.add_command(label="서버메뉴2")
file_menu.add_separator()
file_menu.add_command(label="종료", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

rad_menu = tk.Menu(menu_bar, tearoff=0, selectcolor="red")
rad_menu.add_radiobutton(label="서버메뉴", state="disable")
rad_menu.add_radiobutton(label="서버메뉴2")
rad_menu.add_radiobutton(label="서버메뉴3")
menu_bar.add_cascade(label="라디오메뉴", menu=rad_menu)

chk_menu = tk.Menu(menu_bar, tearoff=0)
chk_menu.add_checkbutton(label="체크메뉴")
chk_menu.add_checkbutton(label="체크메뉴2")
chk_menu.add_checkbutton(label="체크메뉴3")
menu_bar.add_cascade(label="체크메뉴", menu=chk_menu)


win.mainloop()