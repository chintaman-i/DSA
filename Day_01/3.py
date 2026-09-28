num = int(input("Enter a number: "))
sum = 0
n=num

while (num > 0):
    sum=sum*10+(n%10)
    n=n//10  

if(num==sum):
    print("Is palindrome")
else:
    print("not palindrome")