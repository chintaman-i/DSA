#Print pattern
a=int(input("Enter the number of rows(odd numbers): "))
if a%2==0:
    print("Please enter odd number")


else:
    mid=a//2

    for i in range(a):
        for j in range(a):
            if i == mid or j == mid:
             print("*", end=" ")
            else:
             print(" ", end=" ")
        print()
