n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(0,n-1,2):
    k=arr[i+1]
    while(k!=0):
        l.append(arr[i])
        k-=1 
print(*l)
