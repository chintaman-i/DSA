#Enter a number to get prime numbers

num=int(input("Enter a number to get prime numbers"))

flag=0

for i in range(2,(num//2)+1):
    if(num%i==0):
        flag=1

    break

if(flag==1):
    print("number is prime")
else:
    print("number is not prime")
