a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    k=len(str(i))
    p=len(set(str(i)))
    if(k==p):
        c+=1 
print(c)
