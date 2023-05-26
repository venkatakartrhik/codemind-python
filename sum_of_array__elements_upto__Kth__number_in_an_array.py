n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=[i for i in l if i<=m]
print(sum(c))