n=int(input())
l=list(map(int,input().split()))
k=[]
j=[]
p=[]
for i in l:
    if i not in k:
        k.append(i)
    else:
        j.append(i)
for i in k:
    if i not in j:
        p.append(i)
if len(p)!=0:
    print(*p)
else:
    print(-1)