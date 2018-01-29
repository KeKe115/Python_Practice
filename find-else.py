# for構文でelseを記述する場合
# 食材の一覧
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "Cabbage"]

# マンゴーがないか確認
for food in foodstuff:
    if food == "Mango":
        print("マンゴーが入っています")
        break
else:
    printf("ありません")

