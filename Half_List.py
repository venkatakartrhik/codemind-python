n=int(input())
l=list(map(int,input().split()))
f=l[:n//2]
s=l[n//2:]
s_l=s[::-1]
x=s_l+f
print(*x)