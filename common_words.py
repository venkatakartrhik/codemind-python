s1=input().lower()
s2=input().lower()
s1=s1.split()
s2=s2.split()
k=[]
for i in s2:
    if i  in s1:
        k.append(i)
print(*k)