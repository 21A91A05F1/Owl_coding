n=int(input())
s="" 
while(n!=0):
    for i in range(9,-1,-1):
        if(i<=n):
            s+=str(i)
            n-=i 
s=s[::-1]
s=s[1:]
print(s)
