n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n):
    if l[i]%2==0:
        m+=l[i]
    else:
        break
print(m)