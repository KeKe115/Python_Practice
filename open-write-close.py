# ファイルを開く
a_file = open("test.txt", mode="w", encoding="utf-8")

# ファイルに書き込む
a_file.write("人がゴミのようだ\n")
a_file.write("事を急ぐと元も子もなくしますよ\n")
a_file.write("３分間待ってやる\n")

# ファイルを閉じる
a_file.close()

