def rev(n):
    return n[::-1]
s=input()
l=list(s.split())
r=l[::-1]
for i in r:
    print(rev(i),end=" ")