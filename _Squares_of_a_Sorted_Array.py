n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    s.append(i*i)
print(*(sorted(s)))