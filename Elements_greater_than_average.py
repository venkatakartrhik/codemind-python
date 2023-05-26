n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
s=[i for i in l if i>=a]
print(len(s))