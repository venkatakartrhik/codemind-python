s1=input().lower()
s2=input().lower()
c=[]
for i in s1:
    if i in s2 and i not in c and i !=' ':
        c.append(i)
if len(c)!=0:
    a=[]
    for i in c:
        if i.isalpha():
            a.append(i)
            a.sort()
    for i in a:
        print(i,end='')
else:
    print(-1)