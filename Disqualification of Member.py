def moon(l: list, i=1):
    if len(l) == 1:
        return l
    elif i % 2 != 0:
        r = []
        for j in range(1, len(l), 2):
            r.append(l[j])
        return moon(r, i + 1)
    else:
        l.reverse()
        r = []
        for j in range(1, len(l), 2):
            r.append(l[j])
        r.reverse()
        return moon(r, i + 1)
n = int(input())
a = moon([i for i in range(1, n + 1)])
print(a[0])
'''
Disqualification of Member
Program Description :
You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. Apply the following algorithm on arr:

1 . Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
2 . Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
3 . Keep repeating the steps again, alternating left to right and right to left, until a single number remains. 

Input Format :
The program should accept a single input integer N, representing the maximum number in the list.

Output Format :
The program should return an integer, which is the last remaining number after applying the algorithm to the list of integers from 1 to N.

Input :
N = 9 


Output :
6 


Constraints :
1 ≤ N ≤ 10^5 
'''
