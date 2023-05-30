n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
p=[]
k=[]

for i in l1:
    if i not in l2:
        p.append(i)
for j in l2:
    if j not in l1:
        k.append(j)

print(len(set(p+k)))