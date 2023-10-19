def is_prime(n):
    if(n<=1):
        return 0 
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0 
    return 1
n=int(input())
l=list(map(int,input().split()))
c=0 
s=0 
for i in l:
    if is_prime(i):
        c+=1 
        s+=i 
print("%.2f"%(s/c))
