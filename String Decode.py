def com(s):
    c=""
    cnt=1
    for i in range(1,len(s)):
        if(s[i]==s[i-1]):
            cnt+=1
        else:
            c+=s[i-1]+str(cnt)
            cnt=1
    c+=s[-1]+str(cnt)
    return c
s=input()
k=fun(s)
if(len(k)<=len(s)):
     print('Yes')
else:
    print('No')
