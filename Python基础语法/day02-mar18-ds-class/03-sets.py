numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}
second.add(5)
second.remove(4)
print(second)
print(uniques)

print(uniques | second)  # 并集
print(uniques & second)  # 交集
print(uniques - second)  # 差集
print(uniques ^ second)  # 对称差集

uniques.update([4, 9])  # 更新集合
print(uniques)

uniques.clear()  # 清空集合

# 判断两个集合是否相交
print(s1.isdisjoint(s3))  # 输出：False
# 判断一个集合是否为另一个集合的子集
print(s3.issubset(s1))  # 输出：True
# 判断一个集合是否为另一个集合的超集
print(s1.issuperset(s3))  # 输出：True
