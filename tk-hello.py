# tkinterを取り込む
from tkinter import *
import tkinter.messagebox as mb

# ボタンが押された時の動作を関数として定義
def say_hello():
    mb.showinfo("挨拶", "おはようございます")    # [OK]ボタンがあるだけのダイアログ

# メインウィンドウを作成
root = Tk()
root.title("挨拶")    # メインウィンドウのタイトルを設定

# ラベルを作成
desc_label = Label(text = "以下のボタンを押して下さい")
desc_label.pack()

# 挨拶ボタンを表示
hello_button = Button(text = "挨拶", width = 10, height = 10, command = say_hello)

hello_button.pack()

# メインループを開始
root.mainloop()

