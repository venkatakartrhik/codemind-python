n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if i%2!=0 and i not in x:
        x.append(i)
print(sum(x))