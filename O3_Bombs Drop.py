'''
LEVEL-3/HARD/POINTS: 80
Bombs Drop
Program Description :
In Chefland, there are N houses numbered from 1 to N, ith house has a defence system having strength Ai.

Chef suspects a bomb drop on one of the houses very soon. A bomb with attack strength X can destroy the ith house, if the defence system of the ith house Ai, is strictly less than X.

Also, when the ith house is destroyed due to the bomb, all houses with indices j such that 1≤j 

Given one bomb with attack strength X, find the maximum number of houses that can get destroyed. 

Input Format :
The first line will contain T - the number of test cases. Then the test cases follow.

The first line of each test case contains 2 integers N,X.

The second line of test case contains N space separated integers A1,A2,…,AN.

Output Format :
For each test case, output in a single line the maximum number of houses that can get destroyed if the bomb can hit any house.

Input :
2

8 6

4 1 6 1 6 5 6 8

2 1

3 5


Output :
6

0


Constraints :
1<= T <=100

1<= N <=105

1<= X <=109

1<= Ai <=109 
'''
t=int(input())
while(t!=0):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(len(l)-1,-1,-1):
        if(l[i]<x):
            print(i+1)
            break 
    else:
        print(0)
    t-=1
