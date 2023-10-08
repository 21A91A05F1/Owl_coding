def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0 
    return 1 
t=int(input())
while(t):
    n=int(input())
    c=0
    p=1 
    for i in range(2,n+1):
        if is_prime(i):
            if(p*i<=n):
                p*=i
                c+=1
            else:
                break
    print(c)
    t-=1 
