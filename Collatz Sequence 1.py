n = int(input())
l = []
l.append(n)
while(n!=1):
    if n%2 == 0:
        n = n//2
        l.append(n)
    else:
        n = 3*n+1
        l.append(n)
print(*l)
'''
LEVEL-2/MEDIUM/POINTS: 40
Collatz Sequence 1
Program Description :
Take any positive non-zero integer N.

If N is even do N / 2,
If N is odd do 3 * N + 1.

If we keep on doing the above steps every N, will reach 1 at one point. And the sequence formed by the number N to reach 1 is called as Collatz Sequence. 

Input Format :
A single line contains an integer N.

Output Format :
Print the Collatz Sequence.

Input :
3


Output :
3 10 5 16 8 4 2 1


Constraints :
1<= N <=10^6
'''
