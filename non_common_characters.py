s1=input().lower()
s2=input().lower()
a=[]
for i in s1:
    if i not in s2 and i not in a and i!=" ":
        a.append(i)
for i in s2:
    if i not in s1 and i not in a and i!=" ":
        a.append(i)
c=[]
for i in a:
    if i.isalpha():
        c.append(i)
        c.sort()
for i in c :
    print(i,end='')