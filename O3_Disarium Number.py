n=int(input())
temp=n
rev=0
res=0
c=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
n=temp
while(rev>0):
    d1=rev%10
    c+=1
    res=res+d1**c
    rev=rev//10
if(res==temp):
    print("True")
else:
    print("False")
  '''
  Disarium Number
Program Description :
You are developing a program for a digital puzzle game. In this game, players are given a challenge to identify Disarium numbers. A Disarium number is defined as a number where the sum of its digits, each raised to the power of their respective positions, equals the number itself. For example, 89 is a Disarium number because 8^1 + 9^2 = 8 + 81 = 89.

Input Format :
A single line contains an integer N.

Output Format :
Display True if the Number is Disarium Number else display False if Not Disarium Number.
 

Input :
89


Output :
True


Constraints :
1<= N <=10^6
  '''
