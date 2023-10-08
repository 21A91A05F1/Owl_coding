n=int(input())
t=[-1]*n
l=list(map(int,input().split()))
c=0
while(l!=t):
    p=-1
    for i in range(n):
        if p==-1 and l[i]!=-1:
            p=l[i]
            l[i]=-1
        elif p!=-1 and l[i]!=-1 and p>l[i]:
            p=l[i]
            l[i]=-1
    c+=1
print(c)
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
