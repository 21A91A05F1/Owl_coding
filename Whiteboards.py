t=int(input())
while(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(m):
        a=sorted(a)
        a[0]=b[i]
    print(sum(a))
    t-=1 
