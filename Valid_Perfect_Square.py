n=int(input())
l=[]
for i in range(0,n):
    a=int(input())
    l.append(a)
for i in range(0,n):
    c=0
    for j in range(0,l[i]):
        if j*j==l[i]:
            c+=1
    if c>0:
        print("True")
    else:
        print("False")