'''
LEVEL-3/HARD/POINTS: 80
String Protocol
Program Description :
An input string S of length N is transferred through the network using a special protocol. The protocol can send the string through a series of operations. In one operation, we can choose a lowercase english alphabet C and do one of the following:

Transfer 1 copy of C through the network.
Transfer 2 copies of C through the network.
Each of the above transfers take 1 unit of time.

Find the minimum time in which we can transfer the entire string S through the network. 

Input Format :
The first line will contain T - the number of test cases. Then the test cases follow.
The first line of each test case contains N - the length of the string S.
The second line of each test case contains the string S. 

Output Format :
For each test case, output in a single line, the minimum time required to transfer the string.
 

Input :
2

5

cbcdc

6

aabeee


Output :
5

4


Constraints :
1≤T≤100
1≤N≤10^5 
'''
t=int(input())
while(t):
    n=int(input())
    s=input()
    i,c=0,0
    while(i!=n):
        if(i!=n-1 and s[i]==s[i+1]):
            i+=2 
            c+=1 
        else:
            i+=1 
            c+=1 
    print(c)
    t-=1 
