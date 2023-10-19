s=input()
c=0 
for i in s:
    if i.isdigit():
        c+=1
if(c):
    print('Contains',c,'digit')
else:
    print("Doesn't contain digit")
