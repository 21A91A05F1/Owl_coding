def fun(n):
    s=0 
    for i in range(1,n+1):
        if(n%i==0):
            s+=i 
    return s

a=int(input())
b=int(input())
a1=fun(a)
a2=fun(b)
if(a1==a2):
    print("Amicable")
else:
    print("Not Amicable")
