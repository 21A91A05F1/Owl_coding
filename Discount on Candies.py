n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
l=l[::-1]
s=0
for i in range(n):
    if((i+1)%3==0):
        continue 
    s+=l[i]
print(s)    
