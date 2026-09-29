#find the smallest and largest elements:wap to accept n integers into an array and find and
#display the largest element second largest smallest elemnt,second smallest elemnt present in the array

n = int(input("Enter the length of array: "))
a = []

for i in range(1, n + 1):
    b = int(input("Enter the array element: "))
    a.append(b)

print(a)

largest = a[0]
slargest = a[0]
smallest = a[0]
ssmall = a[0]

for i in a:
    if i > largest:
        slargest = largest
        largest = i
    elif i > slargest and i != largest:
        slargest = i

    if i < smallest:
        ssmall = smallest
        smallest = i
    elif i < ssmall and i != smallest:
        ssmall = i

print(largest)
print(slargest)
print(smallest)
print(ssmall)
