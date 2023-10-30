'''
LEVEL-3/MEDIUM/POINTS: 40
Find Possible GCD
Program Description :
Tevitt has two distinct positive integers A and B.

Tevitt wonders how many distinct values are possible for the expression gcd (A+X, B+X), where X can take any non-negative integer value.

Help Tevitt find this value.

Here, gcd stands for Greatest Common Divisor. 

Input Format :
The first line contains a single integer T which indicates no of test cases.

The next T lines contain two integer A and B.

Output Format :
For each testcase, output the number of distinct values of the expression gcd (A+X, B+X), where X can take any non-negative integer value.
 

Input :
2

1 2

12 8


Output :
1

3


Constraints :
1 <= T <= 1000

1 <= A, B <= 10^9 
'''
for _ in range(int(input())):
    a,b=map(int,input().split())
    q=abs(a-b)
    count=0
    for i in range(1,int(q**0.5)+1):
        if q%i==0:
            if q/i == i:
                count+=1
            else:
                count+=2
    print(count)
