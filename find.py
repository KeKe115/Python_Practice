# テキストからキーワードを探す
key = "why"

with open("mt7_7.txt", encoding="utf-8") as tf:
    # 1行ずつファイルを読み込む
    for i, line in enumerate(tf):     # enumerate関数を使う
        # 文字列 key が行に含まれるか?
        if line.find(key) >= 0:
            print(i + 1, ":", line)

