t=int(input())
while(t):
    n=int(input())
    arr=list(map(int,input().split()))
    s=sum(arr)
    ls=0
    for i in arr:
        s-=i 
        if(ls==s):
            print(arr.index(i))
            break
        ls+=i
    else:
        print("-1")
    t-=1 
'''
Equilibrium Index of an Array
Program Description :
You are developing a program for an online marketplace that tracks sales data for various products. You are given an array representing the daily sales of a particular product over a period of time. Your task is to find the index of the first equilibrium point for this product's sales data. An equilibrium point is an index where the sum of sales on the left side of the index is equal to the sum of sales on the right side of the index.

Write a Python function find_equilibrium_index(arr) to find the index of the first equilibrium point in the given sales data array.

Here's the function parameter:

arr (list of integers): The array representing daily sales for the product.

Your function should return the index of the first equilibrium point if one exists. If no equilibrium point is found, return -1.

Input Format :
The first line of input takes an integer T denoting the no of test cases, then T test cases follow. The first line of each test case is an integer N denoting The size of the array. Then in the next line are N space-separated values of the array.
 

Output Format :
For each test case, the output will be the equilibrium index of the array. If no such index exists output will be -1.

Input :
2

4

1 2 0 3

4

1 1 1 1


Output :
2

-1


Constraints :
1<=T<=100
1<=N<=105
-1000<=A[]<=1000 
'''
