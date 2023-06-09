n=int(input())
l=list(map(int,input().split()))
f=l[:n//2]
s=l[n//2:]
k=abs(sum(f)-sum(s))
if k%4==0:
    print("X")
else:
    print("Y")