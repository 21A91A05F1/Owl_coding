s=input().split(" ")
l=[]
for i in s:
    k=i
    k=k[::-1]
    k="".join(k)
    l.append(k)
l=l[::-1]
print(*l)
