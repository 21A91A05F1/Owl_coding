'''
Series of Different Sequences
Program Description :
You are working on a scientific research project that involves analyzing a unique mathematical series. This series is a combination of two geometric sequences, where all the odd-indexed terms form one geometric sequence, and all the even-indexed terms form another geometric sequence. To perform your research effectively, you need to develop a program that can calculate the Nth term in this mixed geometric series.

Problem Statement:

Write a program to find the Nth term in a mixed geometric series. This series consists of two geometric sequences, with odd-indexed terms forming one sequence and even-indexed terms forming another sequence.

Input Format :
The program should accept a single integer input, N representing the position of the term you want to find in the series.

Output Format :
The program should output the Nth term in the series.

Input :
10


Output :
3 -2 5 2 11 22 29 122 83 622 245 


Constraints :
1 ≤ N ≤ 50
'''
n = int(input())
odd = [3, 5]
for i in range(1, n):
    diff = odd[i] - odd[i - 1]
    answer = (diff * 3) + odd[i]
    odd.append(answer)
even = [-2, 2, 22]
for i in range(2, n):
    diff = even[i] - even[i - 1]
    answer = (diff * 5) + even[i]
    even.append(answer)
r = []
for i in range(n):
    r.append(odd[i])
    r.append(even[i])
print(*r[: n + 1])
