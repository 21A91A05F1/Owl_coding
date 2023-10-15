s=input().split(" ")
a,b=[],[]
for i in s:
    k=i 
    a.append(max(k))
    b.append(min(k))
#print(a,b)
res=[]
for i in range(len(a)):
    x=ord(a[i])
    y=ord(b[i])
    res.append(abs(x-y))
print(*res)
