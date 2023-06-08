n=int(input())
l=list(map(int,input().split()))
s=[]
k=[]
for i in l:
    if i not in k:
        k.append(i)
    else:
        s.append(i)
print(*s)