#Print pattern
a = 7
b = 7

mid_row = a // 2
mid_col = b // 2

for i in range(a):
    for j in range(b):
        if i == mid_row or j == mid_col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
