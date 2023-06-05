t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x=l1+l2
    k=sorted(x)
    print(*k)