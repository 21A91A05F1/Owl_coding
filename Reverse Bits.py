def fun(n):
    n=bin(n)[2:]
    while(len(n)<32):
        n='0'+n
    n=n[::-1]
    return int(n,2)
n=int(input())
print(fun(n))
