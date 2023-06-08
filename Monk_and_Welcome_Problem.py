n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(l1[i]+l2[i])
print(*s)