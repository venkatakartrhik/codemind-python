def prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
t=int(input())
for _ in range(t):
    n=int(input())
    l=[i for i in range(n-5,n+5) if prime(i)]
    k=[abs(n-j) for j in l]
    m=min(k)
    print(l[k.index(m)])