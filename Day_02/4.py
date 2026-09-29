#Serach an Elemnt:WAP to accept the n integers into an array and search for given number in the array
#display the position of the  and if present or not
n=int(input("Enter the length of array: "))
a=[]

for i in range(1,n+1):
    b=int(input("Eneter the array elements: "))
    a.append(b)

print(a)

b=int(input("Enter a number to search: "))

if b in a:
    print("Element Found a Positon:",a.index(b)+1)

else:
     print("element not found")

