s1=input()
s2=input()
#print(s1,s2)
s1=sorted(s1+s2)
s=""
for i in s1:
    if i!=" ":
        s+=i 
print(s)
