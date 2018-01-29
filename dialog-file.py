import tkinter.filedialog as fd

# ファイル選択ダイアログを表示
path = fd.askopenfilename(title = "処理対象のファイルを指定して下さい", # ダイアログ上部のタイトルを設定
    filetypes = [('HTML', '.html')])  # 「HTML」または「html」形式のファイルだけを表示
print(path)

