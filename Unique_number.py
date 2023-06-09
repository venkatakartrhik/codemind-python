n=int(input())
m=str(n)
s=[]
k=[]
for i in m:
    if i not in s:
        s.append(i)
    else:
        k.append(i)
if len(k)==0:
    print("Unique Number")
else:
    print("Not Unique Number")