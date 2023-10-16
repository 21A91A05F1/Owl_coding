def is_pali(s):
    if(s==s[::-1]):
        return 1 
    return 0
t=int(input())
while(t):
    a=input()
    if(is_pali(a)):
        if(len(a)%2==0):
            print("YES","EVEN")
        else:
            print("YES","ODD")
    else:
        print("NO")
    t-=1 
