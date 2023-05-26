n=int(input())
l=list(map(int,input().split()))
s=len(l)
c=0
for i in l:
    if i%2==0 or i==0:
        c+=1
if c==s:
    print(True)
else:
    print(False)