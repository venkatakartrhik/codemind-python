def neon(x):
    s=0
    while x:
        d=x%10
        x=x//10
        s=s+d
    return s
n=int(input())
x=n*n
s=neon(x)
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")