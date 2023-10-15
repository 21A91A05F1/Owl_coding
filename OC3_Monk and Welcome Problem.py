n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in range(n):
    res.append(a[i]+b[i])
print(*res)
