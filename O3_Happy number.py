def fun(n):
    s=0
    while(n>=10 and n!=0):
        s=0
        while(n):
            d=n%10
            s=s+d**2
            n=n//10
        n=s
    if(n==1 or n==7):
        return "True"
    else:
        return "False"
n=int(input())
print(fun(n))
