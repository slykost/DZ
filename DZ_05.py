a = int(input())
b = a % 10          #123 % 10 = 3
c = (a - b) // 10   #(123-3)//10=12
d = c % 10          #12%10=2
e = (c - d) // 10   #(12-2)//10=1
print(b, d, e, sep='')

