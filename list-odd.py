# 10以下の奇数を持つリストを作る
# 2倍して1を引く方法
data = [(i * 2 - 1) for i in range(1, 6)]
print(data)

# rangeを工夫する方法
data = [i for i in range(1, 11, 2)]
print(data)

# 内包表記でforとiを組み合わせる方法
data = [i for i in range(1, 11) if i % 2 == 1]
print(data)

