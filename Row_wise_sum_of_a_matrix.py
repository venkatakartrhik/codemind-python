n,m=map(int,input().split())
mat=[]
for k in range(n):
    x=list(map(int,input().split()))
    mat.append(x)
for i in range(n):
    s=0
    for j in range(m):
        s+=mat[i][j]
    print(s,end=" ")