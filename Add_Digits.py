def adddigit(num):
    s=0
    while num:
        d=num%10
        num=num//10
        s=s+d
    return s
n=int(input())
while n>9:
    n=adddigit(n)
print(n)