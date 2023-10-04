n=int(input())
l=list(map(int,input().split()))
p=[]
for i in set(l):
    p.append(l.count(i))
m=max(p)
c=0
res=0
for i in set(l):
    if(l.count(i)==m):
        c+=1
        res=i
if(c==1):
    print("Yes")
    print(res)
else:
    print("No")
