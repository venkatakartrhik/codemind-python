n=int(input())
lst=list(map(int,input().split()))
o=[i for i in lst if i%2!=0]
print(o[-1])