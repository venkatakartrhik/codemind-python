n=int(input())
lst=list(map(int,input().split()))
e=[i for i in lst if i%2==0]
print(e[-1])