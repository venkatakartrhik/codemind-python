n=int(input())
l=list(map(int,input().split()))
s1=[]
s2=[]
for i in l:
    if i!=0:
        s1.append(i)
    else:
        s2.append(i)
s=s1+s2
print(*s)