def fun(n):
    temp=n
    c=0
    while(temp!=0):
        d=temp%10 
        if(d!=0 and n%d==0 ):
            c+=1 
        temp//=10
    if(c==len(str(n))):
        return 1
    return 0
a=int(input())
b=int(input())
l=[]
for i in range(a,b+1):
    if(fun(i)):
        l.append(i)
print(*l)
