s1=input().lower()
s2=input().lower()
n=s1.split()
m=s2.split()
a=[]
for i in n:
    if i in m and i not in a and i!=' ':
        a.append(i)
for i in n:
    if i in m and i not in a and i!=' ':
        a.append(i)
print(len(a))