s=input()
v="aeiou"
c,m=0,0
for i in s:
    if i in v:
        c+=1 
        m=max(m,c)
    else:
        c=0
print(m)
