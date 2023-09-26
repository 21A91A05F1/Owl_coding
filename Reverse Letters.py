s=input() 
l=[]
for i in s:
    if i.isalpha():
        l.append(i)
res=''
for i in s:
    if i.isalpha():
        res+=l.pop()
    else:
        res+=i
print(res)
'''
Input :
abc-abc


Output :
cba-cba
'''
