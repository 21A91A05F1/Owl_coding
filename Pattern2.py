'''
A

BB

CCC

DDDD

EEEEE 
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end="")
    print()
    
