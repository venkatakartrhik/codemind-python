n=int(input())
n1,n2=0,1
n3=n1+n2
while n3<n:
    n3=n1+n2
    n1=n2
    n2=n3
if n3==n:
    print("True")
else:
    print("False")