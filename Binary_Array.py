n=int(input())
l=list(map(int,input().split()))
k=len(l)
c=0
for i in l:
    if i==0 or i==1:
        c+=1
if c==k:
    print(True)
else:
    print(False)