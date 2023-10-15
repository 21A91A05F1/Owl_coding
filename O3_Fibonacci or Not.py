def fun(n):
    l=[10]*n
    l[0]=0
    l[1]=1
    for i in range(2,n):
        l[i]=l[i-1]+l[i-2]
    return l 
n=int(input())
l=fun(n)
if n in l:
    print("True")
else:
    print("False")
