# for文と同じ働きをする関数を自作
def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

# リストの内容を全て画面に表示
nums = [1, 2, 3]
for_func(nums, lambda i : print(i))

# 辞書型の内容を全て画面に表示
ages = {"Taro":20, "Jiro":15, "Saburo":18}
for_func(ages.items(), lambda n :print(n))

