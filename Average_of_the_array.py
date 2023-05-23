n=int(input())
lst=list(map(int,input().split()))
c=[i for i in lst]
t=sum(c)/n
print("%0.2f"%t)