'''
Input :
Thi$ is s@mple


Output :
Thi$ is e@lmps


Constraints :
1< len(s) <=10^5
'''
a=input().split(" ")
b="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans=" "
for i in a:
    c=[]
    for j in i:
        if j in b:
            c.append(j)
    c.sort()
    k=0
    for j in i:
        if j in b:
            ans+=c[k]
            k+=1 
        else:
            ans+=j 
    ans+=" "
print(ans)
