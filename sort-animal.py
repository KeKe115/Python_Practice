# (動物, 最高時速)のリスト
animal_list = [
    ("ライオン", 58),
    ("チーター", 110),
    ("シマウマ", 60),
    ("トナカイ", 80),
]

# 足の早い順に並び替える
faster_list = sorted(animal_list, key=lambda ani : ani[1], reverse = True)

# 結果を表示
for i in faster_list:
    print(i)

