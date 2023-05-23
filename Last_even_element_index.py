n=int(input())
lst=list(map(int,input().split()))
e=[i for i in range(n) if lst[i]%2==0]
print(max(e))