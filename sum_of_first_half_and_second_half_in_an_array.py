n=int(input())
lst=list(map(int,input().split()))
print(sum(lst[0:(n//2)]))
print(sum(lst[(n//2):]))