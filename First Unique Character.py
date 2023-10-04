s=input()
f=0
for i in range(len(s)):
    for j in range(len(s)):
        if(s[i]==s[j] and (i!=j)):
            break 
    else:
        print(s[i])
        f=1
        break 
if(f==0):
    print("-1")
