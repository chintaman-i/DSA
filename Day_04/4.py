# alphabet pattern

n=int(input("Enter the number of rows: "))
num=0

for i in range(n):
    print(' '*(n-i-1), end='')
    for j in range(2*i+1):
        print(chr(65+j), end='')
    print()