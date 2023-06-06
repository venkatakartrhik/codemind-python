n=input().split()
c=0
for i in n:
    if i[0] in "aeiouAEIOU":
        if i[-1] not in "aeiou":
            c+=1
print(c)
