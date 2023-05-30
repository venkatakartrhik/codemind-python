n=int(input())
l=list(map(int,input().split()))
k=sorted(l)
if l==k[::-1]:
    print("yes")
else:
    print("no")