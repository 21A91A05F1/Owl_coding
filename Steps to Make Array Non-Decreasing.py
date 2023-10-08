n=int(input())
s=list(map(int,input().split()))
ans=0
m=s[0]
pre=-1
c=0
for i in range(len(s)):
    if(m<=s[i]):
        m=s[i]
        ans=max(ans,c)
        c=0
        pre=-1
    else:
        c+=1
        if(pre!=-1 and pre>s[i]):c-=1
        pre=s[i]
ans=max(ans,c)
print(ans)
