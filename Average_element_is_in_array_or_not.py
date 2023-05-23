n=int(input())
lst=list(map(int,input().split()))
s=[i for i in lst]
t=sum(s)//n
print(t in lst)
