n,k=map(int,input().split())
k=k%n
arr=list(map(int,input().split()))
res=arr[-k:]+arr[:-k]
print(*res)
