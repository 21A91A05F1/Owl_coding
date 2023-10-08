#Towers-->28
n=int(input())
l=list(map(int,input().split()))
ans=[]
ans.append(l[0])
for i in range(1,n):
    if ans[-1]<=l[i]:
        ans.append(l[i])
    else:
        ans.sort()
        for j in range(len(ans)):
            if l[i]<ans[j]:
                ans[j]=l[i]
                break
print(len(ans))
'''
Towers
Program Description :
You are a construction engineer working on a project that involves building towers with cubes. You have a specific set of cubes provided in a certain order, and you must follow certain rules while building the towers. Whenever two cubes are stacked on top of each other, the upper cube must be smaller than the lower cube. Your task is to create a function that calculates the minimum possible number of towers you can build with these cubes while processing them in the given order.

Problem Statement:

Write a program to calculate the minimum possible number of towers that can be built with a given set of cubes while following the rule that the upper cube must be smaller than the lower cube. The cubes must be processed in the order they are given.

Input Format :
The program should accept a single input: a list of integers cubes, representing the sizes of the cubes in the order they are provided. The length of the cubes list can be up to 1000.

Output Format :
The program should return an integer, which is the minimum possible number of towers that can be built while processing the cubes in the given order.

Input :
5

3 8 2 1 5  


Output :
2


Constraints :
Each cube's size is in the range of 1 to 1000.

The length of the cubes list can be up to 1000.
'''
