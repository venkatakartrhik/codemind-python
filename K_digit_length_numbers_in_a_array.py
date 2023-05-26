def count(n):
    c=0
    s=str(n)
    for i in s:
        if i.isdigit():
            c+=1
    return(c)
n,m=map(int,input().split())
l=list(map(int,input().split()))
k=0
for i in l:
    if m==count(i):
        k+=1
print(k)
    