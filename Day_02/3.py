#count Even And Odd Numbers:WAP to accept n integers into an array and count the and diplay the number of even and odd numbers in the array

n=int(input("Enter the length of array: "))
a=[]
odd=0
even=0
for i in range(1,n+1):
    b=int(input("Eneter the array elements: "))
    a.append(b)

print(a)

for i in a:
    if i/2==0:
        even =even+1
    else:
        odd=odd+1

print(odd)
print(even)
