n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
p=[]
k=[]
for i in l1:
    if i in l2:
        p.append(i)
for i in l2:
    if i in l1:
        k.append(i)
print(len(set(p+k)))