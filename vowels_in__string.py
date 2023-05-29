n=input()
m=[]
for i in n:
    if i in "aeiouAEIOU" and i not in m:
        m.append(i)
if len(m)!=0:
    print(*m)
else:
    print(-1)