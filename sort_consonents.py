def fun(s):
    v=0
    for i in s:
        if i in 'aeiouAEIOU':
            return True
    return False
n=list(input().split())
for k in range(len(n)):
    x=[]
    l=list(n[k])
    for i in range(len(l)):
        if fun(l[i])==False:
            x.append(l[i])
            l[i]="*"
    x.sort()
    a=0
    for j in range(len(l)):
        if l[j]=="*":
            l[j]=x[a]
            a+=1
    print(''.join(l),end=" ")