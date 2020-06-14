x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (x1 + 2 == x2 and y1 + 1 == y2) or (x1 + 2 == x2 and y1 - 1 == y2):
    print("YES")
elif (x1 - 2 == x2 and y1 + 1 == y2) or (x1 - 2 == x2 and y1 - 1 == y2):
    print("YES")
elif (x1 + 1 == x2 and y1 + 2 == y2) or (x1 + 1 == x2 and y1 - 2 == y2):
    print("YES")
elif (x1 - 1 == x2 and y1 + 2 == y2) or (x1 - 1 == x2 and y1 - 2 == y2):
    print("YES")
else:
    print("NO")