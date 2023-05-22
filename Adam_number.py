
def reverse(num):
    rev=0
    while num:
        d=num%10
        num=num//10
        rev=rev*10+d
    return rev
n=int(input())
s1=n**2
r=reverse(n)
s2=r**2
if s1==reverse(s2):
    print("True")
else:
    print("False")