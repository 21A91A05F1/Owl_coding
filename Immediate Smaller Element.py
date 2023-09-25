n=int(input())
arr=list(map(int,input().split()))
res=[]
for i in range(n-1):
    if(arr[i]>arr[i+1]):
        res.append(arr[i+1])
    else:
        res.append("-1")
res.append("-1")
print(*res)
