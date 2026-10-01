#Print pattern
a=int(input("Enter the number of rows(odd numbers): "))
if a%2==0:
    print("Please enter odd number")
else:
    b=a
    mid_row = a // 2
    mid_col = b // 2

    for i in range(a):
     for j in range(b):
        if i == mid_row or j == mid_col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
