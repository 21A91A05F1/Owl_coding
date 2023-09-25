def fun(n,k,arr):
    c={}
    for i in arr:
        if i in c:
            c[i]+=1
        else:
            c[i]=1 
        if(c[i]==k):
            return i
    else:
        return -1

n,k=map(int,input().split())
arr=list(map(int,input().split()))
res=fun(n,k,arr)
print(res)
