import tkinter as tk 

win = tk.Tk()
win.title("파이썬 GUI - Frame")
win.geometry("640x400")
win.resizable(False,False)

frame1 = tk.Frame(win, bd=2, relief="solid", background="yellow")
frame1.pack(side="left", fill = "both", expand=True)

frame2 = tk.Frame(win, bd=2, relief="solid", background="blue", pady=30)
frame2.pack(side="right", fill = "both", expand=True)

btn1 = tk.Button(frame1, text="프레임1")
btn1.pack(side="right")

btn2 = tk.Button(frame2, text="프레임2")
btn2.pack()

win.mainloop()
