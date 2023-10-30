n=int(input())
r=" "
while(n>0):
    k=(n-1)%26
    r=chr(65+k)+r
    n//=26
print(r)
