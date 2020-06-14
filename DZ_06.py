N = int(input())
a = 2
b = 1
while a <= N:
    b += 1
    a *= 2
print(b - 1, a // 2, sep=' ')