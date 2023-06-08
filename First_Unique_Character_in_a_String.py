s=input().lower()
a=[]
for i in s:
    if s.count(i)==1:
        a.append(i)
if len(a)!=0:
    k=a[0]
    print(s.index(k))
else:
    print(-1)