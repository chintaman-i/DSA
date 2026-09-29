#Remove Duplicate Elements:WAP to accept n integers into an array and create a new array containing the only 
# the uinque elements,removing all the duplicate values

n=int(input("Enter the length of array: "))
a=[]

for i in range(1,n+1):
    b=int(input("Eneter the array elements: "))
    a.append(b)

print(a)

b=[]

for i in a:
    if i not in b:
        b.append(i)

print(b)


