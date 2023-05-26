n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
c=0
for  i in range(len(mat)):
    if (sorted(mat[i])==mat[i]) or (mat[i])[::-1]== sorted(mat[i]):
        c+=1
print(c)