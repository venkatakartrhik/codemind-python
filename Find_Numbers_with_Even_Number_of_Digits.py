n=int(input())
l=list(map(int,input().split()))
c=[len(str(i)) for i in l]
s=0
for i in c:
    if i%2==0:
        s+=1
print(s)