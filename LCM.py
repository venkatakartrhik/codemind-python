m,n=map(int,input().split())
for i in range(1,m*n+1):
    if(i%n==0 and i%m==0):
        print(i)
        break