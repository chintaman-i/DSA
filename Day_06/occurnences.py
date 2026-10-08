#string to number of occurences

s=input("Enter a string: ")
arr=[0]*26

for i in range(len(s)):
   arr[ord(s[i]) - 97] += 1

print(arr)

for i in range(len(arr)):
    print(chr(i+97),"=",arr[i])

