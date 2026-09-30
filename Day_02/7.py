#move zeros to end: WAp  to accept n integers move teh zeros to end and keeping the relative order of the list


n=int(input("Enter the length of array: "))
a=[]
new = []

for i in range(1,n+1):
    b=int(input("Eneter the array elements: "))
    a.append(b)

print(a)

for i in a:
    if i != 0:
        new.append(i)

for i in a:
    if i == 0:
        new.append(i)
        
print("After moving zeros:", new)