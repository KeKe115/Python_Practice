value = 100

def changeValue():
    # valueをグローバル宣言
    global value
    # 関数の内側でvalueを変更
    value = 20

changeValue();
print("value=", value)

