t=int(input())
while(t):
    a,b,c=map(int,input().split())
    k=(a-b)+(a-c)
    print(min(k,a))
    t-=1
