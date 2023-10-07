n=int(input())
arr=list(map(int,input().split()))
s=1 
f=0 
arr=sorted(arr)
if(arr[0]!=1):
    f=1 
else:
    for i in range(1,n):
        if(arr[i]>s):
            f=1 
            break 
        else:
            s+=arr[i]
if(f==1):
    print("NO")
else:
    print("YES")
