numbers = [1, 2, 3, 4, 5, 6]
even = [number for number in numbers if number % 2 == 0]
# [2, 4, 6]
multiple = [number * 2 for number in numbers]
# [2, 4, 6, 8, 10, 12]

# 字典推导式
m = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
