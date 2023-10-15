s=input().split(" ")
a,b=[],[]
for i in s:
    k=i 
    a.append(max(k))
    b.append(min(k))
#print(a,b)
s1,s2=0,0
for i in a:
    s1+=ord(i)
for i in b:
    s2+=ord(i)
print(abs(s1-s2))
