n=int(input())
a=n*n
x=int(str(n)[::-1])
b=x*x
if(str(a)==str(b)[::-1]):
    print("True")
else:
    print("False")
