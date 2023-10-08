/*
LEVEL-2/EASY/POINTS: 20
Find Transition Point
Program Description :
Given a sorted array containing only 0s and 1s, find the transition point.

Input Format :
The first line contains an integer N, representing the length of the array.

The second line contains N space-separated integers of the array.

Output Format :
The task is to complete the function transitionPoint() that takes array and N as input parameters and returns the 0 based index of the position where "0" ends and "1" begins. If array does not have any 1s, return -1. If array does not have any 0s, return 0.

Input :
5

0 0 0 1 1


Output :
3


Constraints :
1 ≤ N ≤ 500000

0 ≤ arr[i] ≤ 1
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int one=0;
    int zero=0;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        if(a[i]==1)
        {
            one++;
        }
        else if(a[i]==0)
        {
            zero++;
        }
    }
    if(one >0 && zero>0)
    {
        for(int i=0;i<n;i++)
        {
            if(a[i]==1)
            {
                cout<<i;
                break;
            }
        }
    }
    else if(one==0)
    {
        cout<<-1;
    }
    else if(zero==0)
    {
        cout<<0;
    }

    
}
