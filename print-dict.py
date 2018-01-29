# 辞書型のデータを変数に代入
fruits = {
    "バナナ": 300,
    "オレンジ": 240,
    "いちご": 350,
    "マンゴー": 400
}

# 事象型のデータ一覧を表示
for name in fruits.keys():
    # 値段を得る
    price = fruits[name]
    # 画面に出力
    s = "{0}は、{1}円です。".format(name, price)
    print(s)

