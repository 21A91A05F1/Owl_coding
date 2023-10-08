'''
LEVEL-2/MEDIUM/POINTS: 40
Sequence Series
Program Description :
Consider the series below: {2, 1, 3, 4, 7, 11, 18, and so on} In the above series first two elements are 2 and 1 respectively and other elements are the sum of its two immediately previous elements. The task is to find the minimum number of elements that need to be changed in the given array Arr to make a series as per the above statement. For example: Arr[] = {2, 1, 3, 4, 9, 11, 18} In the given array 5th element (9) needs to be replaced with 7 to make the correct series. This means there is only one element that needs to be replaced in the given array. Hence the output = 1.

Input Format :
The first line contains an integer N represent the length of array.

The second line contains space separated integers in the range of N.

Output Format :
Print the count of numbers that need to change to make a series.

Input :
7
2 1 3 4 9 11 18


Output :
1


Constraints :
1< N <=10^6

1<= N[i] <=10^4
'''
n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(2,n):
    if(a[i-2]+a[i-1]!=a[i]):
        c+=1
        a[i]=a[i-1]+a[i-2]
print(c)
