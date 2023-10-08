n,m,a,b=map(int,input().split())
f=n 
k=f//m 
f=f%m
a1=(k*b+f*a)
a2=n*a 
a3=((n//m)+1)*b 
print(min(a1,a2,a3))
