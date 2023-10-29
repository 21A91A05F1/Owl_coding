s=input().split(" ")
a=[]
b=[]
for i in s:
    k=i 
    a.append(ord(min(k)))
    b.append(ord(max(k)))
print(abs(sum(a)-sum(b)))
