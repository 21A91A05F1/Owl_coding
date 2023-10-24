t=int(input())
while(t):
    a,b=map(int,input().split())
    c=0
    while(a%3!=0 and b%3!=0):
        a=abs(a-b)
        b=abs(a-b)
        c+=1 
    print(c)
    t-=1 
