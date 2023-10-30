'''
LEVEL-3/HARD/POINTS: 80
Even odd Series
Program Description :
Consider the following series

This series is a mixture of 2 series, all the odd terms in this series form a geometric series, and all the even terms in this series form a geometric series. write a program to find the Nth term in the series. 

Input Format :
A single line contains an integer N.

Output Format :
Print the odd and even series based on given input.

Input :
10


Output :
2 0 4 1 8 3 16 9 32 27 64 


Constraints :
1<= N <=10^6
'''
n=int(input())+1
f=0
a=2 
b=0 
while(n!=0):
    if(f==0):
        print(a,end=" ")
        a*=2
        f=1
    else:
        print(b,end=" ")
        if(b==0):
            b=1
        else:
            b*=3 
        f=0

    n-=1 
