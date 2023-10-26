def fun(n):
    l=[0]*(n+1)
    l[0]=1
    l[1]=1
    l[2]=2
    for i in range(3, n+1):
        l[i]=l[i-1]+l[i-2]+l[i-3]
    return l[n]
n=int(input())
print(fun(n))
