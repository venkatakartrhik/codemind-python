n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
s=[]
for i in l:
    if i==m:
        s.append(c)
    c+=1
if len(s)!=0:
    print(s[0],s[-1])
else:
    print(-1,-1)