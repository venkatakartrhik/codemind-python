def square_sum(n):
    sum=0
    while n:
        d=n%10
        n=n//10
        sum+=d*d
    return sum
n=int(input())
x=square_sum(n)
while x>=10:
    x=square_sum(x)
if x==1:
    print("True")
else:
    print("False")