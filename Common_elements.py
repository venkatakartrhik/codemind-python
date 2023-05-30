n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(a)):
    for j in range(len(b)):
        if (a[i]==b[j]):
            c.append(b[j])
for i in range(len(a)):
    for j in range(len(b)):
        if (a[i]==b[j]):
            d.append(a[i])
e=[]
for i in c:
    if i not in e:
        e.append(i)
print(*e)