n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[i for i in l if i>=a and i<=b]
if len(c)==0:
    print(-1)
else:
    print(min(c))