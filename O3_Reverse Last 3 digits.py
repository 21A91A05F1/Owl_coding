n=int(input())
s=str(n)
p,k="",""
for i in range(len(s)):
    if i<3:
        p+=str(s[i])
    else:
        k+=str(s[i])
k=k[::-1]
print(p+k)
