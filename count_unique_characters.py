n=input().lower()
a=n.split(" ")
b=[]
for i in a:
    for j in i:
        if n.count(j)==1:
            b.append(j)
print(len(b))