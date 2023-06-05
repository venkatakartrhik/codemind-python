n=int(input())
m=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
c=0
for i in range(n):
    c+=sum(mat[i])
print(c)