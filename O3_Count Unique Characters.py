n=input().lower()
l=[]
c=0
for i in n:
    if i!=" ":
      l.append(n.count(i))
for i in l:
    if (i==1):
        c=c+1
print(c)
  
