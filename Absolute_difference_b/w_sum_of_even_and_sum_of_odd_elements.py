n=int(input())
lst=list(map(int,input().split()))
e=[i for i in lst if i%2==0]
o=[i for i in lst if i%2!=0]
print(abs(sum(e)-sum(o)))