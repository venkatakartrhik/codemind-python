n=int(input())
l=list(map(int,input().split()))
p=[]
k=[]
for i in l:
    if i not in p:
        p.append(i)
for j in p:
    k.append(j)
    k.append(l.count(j))
print(*k)