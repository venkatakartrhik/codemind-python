def reverse(n):
    return n[::-1]
s=input()
l=list(s.split(" "))
a=l[::-1]
for i in a:
    print(reverse(i),end=" ")