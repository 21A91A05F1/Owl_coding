n=int(input())
arr=list(map(int,input().split()))
m=len(arr)
l=[]
for i in range(m):
    if(arr.count(arr[i])==1):
        l.append(arr[i])
l=sorted(l)
print(*l)
