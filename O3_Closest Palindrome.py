def is_pali(n):
    if(str(n)==str(n)[::-1]):
        return 1
    return 0
def r(n):
    a=n-1
    while(True):
        if(is_pali(a)):
            return a
        a-=1 
def l(n):
    a=n+1
    while(True):
        if(is_pali(a)):
            return a
        a+=1
def fun(n):
    x=r(n)
    y=l(n)
    a=n-x
    b=y-n
    if(a==b):
        print(x,y)
    elif(a>b):
        print(y)
    else:
        print(x)
n=int(input())
fun(n)
