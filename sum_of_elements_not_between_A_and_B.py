n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
x=[i for i in lst if i<a or i>b]
print(sum(x))