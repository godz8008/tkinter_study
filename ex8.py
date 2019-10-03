# Tkinter 주요 위젯

# Button       버튼
# Label        텍스트 또는 이미지 표시
# CheckButton  체크박스
# Entry        단순한 라인 텍스트 박스
# ListBox      리스트 박스
# RadioButton  옵션 버튼
# Message      Label과 비슷하게 텍스트 표시, Label과 달리 자동 래핑 가능
# Scale        슬라이스바
# Scrollbar    스크롤바
# Text         멀티라인을 제공하는 텍스트박스
# Menu         메뉴 Panel
# Menubutton   메뉴 버튼
# Toplevel     새로운 윈도우를 생성할 때 사용.Tk()는 윈도우를 자동으로 생성하는 클래스이다. 
#              여기에 추가로 새로운 윈도우 또는 다이얼로그를 만들경우에 Toplevel을 사용한다.
# Combobox     드롭다운 콤보 상자
# Frame        컨테이너 위젯, 다른 위젯들을 그룹핑 할때
# Canvas       그래프와 점들로 그림을 그릴 수 있는 위젯, 커스텀 위젯을 만들때 사용한다.

import tkinter as tk

# 인스턴스 생성
win = tk.Tk()

win.title("파이썬 GUI")

# 윈도우의 사이즈 조정을 막기위한 메소드
win.resizable(0, 0)

win.mainloop()  # 이벤트 순환문, 이것이 없으면 화면에 GUI가 보이지 않는다.
                # 이벤트가 전달되기를 기다리는 무한 루프라고 볼 수 있다.