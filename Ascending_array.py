n=int(input())
l=list(map(int,input().split()))
if l==sorted(set(l)):
    print("yes")
else:
    print("no")