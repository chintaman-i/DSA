#Reverse The Array: WAP to accept N integrs in the array and display the elements in reverse order without changing the original array

n=int(input("Enter the length of array: "))
a=[]

for i in range(1,n+1):
    b=int(input("Eneter the array elements: "))
    a.append(b)

print(a)

rev_num=a[::-1]
print(rev_num)

