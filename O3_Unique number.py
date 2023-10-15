n=int(input())
l=[]
for i in str(n):
    l.append(i)
if(len(l)==len(set(l))):
    print("Unique Number")
else:
    print("Not Unique Number")
