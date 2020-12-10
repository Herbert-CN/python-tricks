A = {1, 2, 3, 3}
B = {3, 4, 5, 6, 7}

print(A | B) # {1, 2, 3, 4, 5, 6, 7}
print(A & B) # {3}
print(A - B) # {1, 2}
print(B - A) # {4, 5, 6, 7}
# 异或
print(A ^ B) # {1, 2, 4, 5, 6, 7}
print((A ^ B) == ((A - B) | (B - A)))   # True