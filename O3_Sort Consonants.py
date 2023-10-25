'''
Input :
this is sample


Output :
hsit is lampse


Constraints :
1< len(s) <=10^5
'''
a=input()
b='qwrtypsdfghjklzxcvbnmQWERTYPSDFGHJKLZXCVBNM'
ans=''
for i in a.split(' '):
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
    ans+=' '
print(ans)
