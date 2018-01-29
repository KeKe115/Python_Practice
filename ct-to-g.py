# カラットからグラムに変換する
# 変換のもとになる値
per_ct = 0.2
# ユーザから入力を得る
user = input("何カラットですか? ")

# 浮動小数点に変換
ct = float(user)

# 計算する
g = ct * per_ct

# 結果を表示
desc = "{0}カラット = {1}グラム".format(ct, g)
print(desc)

