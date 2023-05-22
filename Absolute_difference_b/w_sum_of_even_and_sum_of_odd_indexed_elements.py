n=int(input())
l=list(map(int,input().split()))
e=l[::2]
o=l[1::2]
print(abs(sum(e)-sum(o)))