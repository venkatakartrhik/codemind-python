def rev(n):
    return n[::-1]
n=input()
l=list(n.split(" "))
m=l[::-1]
for i in m:
    print(rev(i),end=" ")