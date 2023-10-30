def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
n=int(input())
temp=n
n=str(n)
s=0
for i in n:
    s+=factorial(int(i))
if s==temp:
    print("True")
else:
    print("False")
