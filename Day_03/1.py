#cube of sum of n atural numbers

n=int(input("Enter a number to get cube sum: "))
sum=0

for i in range(n):
    sum=(n*(n+1)//2)**2

print(sum)