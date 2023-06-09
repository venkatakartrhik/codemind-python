a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))
s=int(input())
c=0
for i in range(a):
    if l1[i]<=s<=l2[i]:
        c+=1
print(c)