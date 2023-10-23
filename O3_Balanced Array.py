t=int(input())
while(t):
    n=int(input())
    arr=list(map(int,input().split()))
    s=sum(arr)
    ls=0
    for i in arr:
        s-=i 
        if(ls==s):
            print("YES")
            break
        ls+=i
    else:
        print("NO")
    t-=1 
