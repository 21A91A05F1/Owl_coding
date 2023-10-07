n=int(input())
arr=list(map(int,input().split()))
k=int(input())
a=n-k
print(arr[0],*arr[n-k:],*arr[1:n-k])
