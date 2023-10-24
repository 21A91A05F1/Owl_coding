t=int(input())
while(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    s=""
    p=""
    for i in arr:
        s+=str(i)
    for i in range(k,0,-1):
        p+=str(i)
    print(s.count(p))
    t-=1 
