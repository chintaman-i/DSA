#claculate the array sum:wap to accept n integers into an array and calculate and display the sum
#of all integers

n=int(input("Enter the length of array: "))
a=[]
sum=0
for i in range(1,n+1):
    b=int(input("Eneter the array elements: "))
    a.append(b)

print(a)

for i in a:
    sum=sum+i

print(sum)

