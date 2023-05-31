def reverse(num):
    rev=0
    while num:
        d=num%10
        num=num//10
        rev=rev*10+d
    return rev
n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    m.append(reverse(i))
print(*m)