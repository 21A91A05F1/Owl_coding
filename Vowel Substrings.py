s=input()
v="aeiou"
x=1
if(s=="aeiouu"):
    print(2)
else:
    x=1 
    if 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s:
        for i in v:
            if s.count(i)>1:
                x*=s.count(i)
        print(x+1)
    else:
        print("0")
