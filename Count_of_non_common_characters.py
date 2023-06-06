s1=input().lower()
s2=input().lower()
s=""
for i in s1:
    if i not in s2 and i not in s and i!=" ":
        s+=i
for i in s2:
    if i not in s1 and i not in s and i!=" ":
        s+=i
print(len(s)-1)