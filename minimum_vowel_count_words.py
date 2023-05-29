def vowel(n):
    v=0
    for i in n:
        if i in 'aeiou':
            v+=1
    return v
n=list(input().split())
x=[]
for i in n:
    x.append(vowel(i))
a=min(x)
print(x.count(a))