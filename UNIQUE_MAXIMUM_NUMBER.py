n=int(input())
l=list(map(int,input().split()))
k=[]
s=[]
p=[]
for i in l:
    if i not in k:
        k.append(i)
    else:
        s.append(i)
for i in k:
    if i not in s:
        p.append(i)
if len(p)!=0:
    print(max(p))
else:
    print(-1)