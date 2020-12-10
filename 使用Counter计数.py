from collections import Counter

# 对可迭代的对象使用， 字符串
c = Counter("Hello, world")
print(c)
# Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 前N个出现最多的元素
print(c.most_common(2))
# [('l', 3), ('o', 2)]

numbers = [20, 32, 1, 67, 58, 2, 1, 20, 34, 34, 20]
c = Counter(numbers)
print(c)
print(c.most_common(1))

# 对可迭代的对象使用， 字典
c = Counter({'red': 4, 'blue': 2})
print(c)
c.elements()