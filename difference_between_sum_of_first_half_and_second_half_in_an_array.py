n=int(input())
lst=list(map(int,input().split()))
a=(sum(lst[0:(n//2)]))
b=(sum(lst[(n//2):]))
print(abs(a-b))