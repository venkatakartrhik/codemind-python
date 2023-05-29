n=input()
x='aeiou'
l=[]
for i in n:
    if i in x and i not in l:
        l.append(i)
if len(l)==5:
    print(0)
else:
    for j in x:
        if j not in l:
            print(j,end=" ")