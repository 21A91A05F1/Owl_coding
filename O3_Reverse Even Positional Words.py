s=input().split(" ")
l=[]
for i in range(len(s)):
    if i%2==0:
        k=s[i][::-1]
        l.append(k)
    else:
        l.append(s[i])
print(*l)
