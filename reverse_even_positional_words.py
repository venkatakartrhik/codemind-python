def rev(n):
    return n[::-1]
n=list(input().split())
l=[]
for i in n:
    if n.index(i)%2==0:
        i=rev(i)
        l.append(i)
    else:
        l.append(i)
print(*l)

        