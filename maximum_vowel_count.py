def vowel(n):
    v=0
    for i in n:
        if i in 'aeiou':
            v+=1
    return v
n=list(input().split())
l=[vowel(i) for i in n]
print(max(l))