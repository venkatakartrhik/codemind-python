n=int(input())
for i in range(n):
    m=int(input())
    s=str(m)
    if s==s[::-1]:
        print(True)
    else:
        print(False)