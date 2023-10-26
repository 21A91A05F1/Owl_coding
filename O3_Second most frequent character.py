s=input()
a,b,c=[],[],[]
for i in s:
    a.append(s.count(i))
x=max(a)
for i in s:
    if s.count(i)!=x:
        b.append(s.count(i))
if(len(b)==0):
    print("-1")
else:
    y=max(b)
    for i  in s:
        if s.count(i)==y:
            print(i)
            break
