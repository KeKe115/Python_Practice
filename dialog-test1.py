import tkinter.messagebox as mb

ans = mb.askyesno("テスト", "Who are you?")

if ans == True:
    mb.showwarning("ああ", "いい")
else:
    mb.showerror("うう", "ええ")

