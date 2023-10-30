'''
LEVEL-3/MEDIUM/POINTS: 40
Choose wisely
Program Description :
There are two problems in a contest.

Problem A is worth 500 points at the start of the contest.
Problem B is worth 1000 points at the start of the contest.

Once the contest starts, after each minute:
Maximum points of Problem A reduce by 2 points .
Maximum points of Problem B reduce by 4 points.

It is known that Professor requires X minutes to solve Problem A correctly and Y minutes to solve Problem B correctly.

Find the maximum number of points Professor can score if he optimally decides the order of attempting both the problems. 

Input Format :
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the time required to solve problems A and B in minutes respectively. 

Output Format :
For each test case, output in a single line, the maximum number of points Professor can score if he optimally decides the order of attempting both the problems.
 

Input :
4

10 20

8 40

15 15

20 10


Output :
1360

1292

1380

1400


Constraints :
1≤T≤1000
1≤X,Y≤100 
'''
t=int(input())
while(t):
    x,y=map(int,input().split())
    a1=500-2*x 
    a2=1000-6*y
    l=a1+a2 
    b1=500-6*x 
    b2=1000-4*y 
    m=b1+b2
    print(max(l,m))
    t-=1 
