n=int(input())
l=list(map(int,input().split()))
m=int(input())
x=[]
for i in l:
    if l.count(i)==m and i not in x:
        x.append(i)
if len(x)!=0:
    print(*x)
else:
    print("-1")