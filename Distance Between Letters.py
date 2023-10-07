s=input().lower()
l=list(map(int,input().split()))
c=0
r=set(s)
for i in range(len(s)):
    m=ord(s[i])-97 
    for j in range(i+1,len(s)):
        if(s[i]==s[j]):
            d=abs(j-i-1)
            if(d==l[m]):
                c+=1 
if(c==len(r)):
    print("true")
else:
    print("false")
