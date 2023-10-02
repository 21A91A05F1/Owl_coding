t=int(input())
while(t!=0):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    s=arr[0]
    ans=1
    for i in range(1,n):
        if(arr[i]>=s):
            ans+=1
            s+=arr[i]
    print(ans)
    t-=1
