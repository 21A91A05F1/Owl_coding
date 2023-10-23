t=int(input())
while(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
   # print(l,k)
    a=-1
    for i in l:
        if i>k:
            a=l.index(i)
            break 
        elif i==k:
            a=l.index(i)
            break
    if(a!=-1):
        print(a)
    else:
        print(n)
    t-=1 
