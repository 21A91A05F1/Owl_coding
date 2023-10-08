#chance of planting a flower-->30
l=list(map(int,input().split()))
k=int(input())
n=len(l)
c=0
for i in range(1,n-1):
    if l[i-1]==0 and l[i+1]==0 and l[i]==0:
        c+=1
        l[i]=1
if l[-1]==0 and l[-2]==0:
    c+=1
if c>=k:
    print('true')
else:
    print('false')
'''
Chance of Planting Flower
Program Description :
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Input Format :
An integer array flowerbed where each element can be either 0 or 1, representing the state of the flowerbed.

An integer N, representing the number of new flowers to be planted.

Output Format :
The program should return True if it's possible to plant n new flowers in the flowerbed without violating the no-adjacent-flowers rule. Otherwise, it should return False.

Input :
1 0 0 0 1

1 


Output :
true


Constraints :
The length of the flowerbed array can be up to 1000.

Each element in flowerbed can be either 0 or 1.

0 ≤ n ≤ 1000.
'''
