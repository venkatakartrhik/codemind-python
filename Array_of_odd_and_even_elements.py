n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
for i in e:
    o.append(i)
print(*o)