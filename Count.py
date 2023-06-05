n=int(input())
l=list(map(int,input().split()))
k=[]
o=[]
e=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
print(len(e),len(o))