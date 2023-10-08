/*
Split Array Largest Sum
Program Description :
You are working on a data analysis project that involves splitting an array into multiple subarrays. In this project, you need to split an array arr of integers into K subarrays in such a way that the maximum sum of any subarray is minimized. Your task is to create a program that can calculate this minimum possible maximum subarray sum.

Problem Statement:

Write a program to split an array arr of size N into K subarrays in such a way that the maximum sum of any subarray is minimized, and then find the minimum possible maximum subarray sum.

Input Format :
first line contains n,k 

second line contains n spaced integers 

Output Format :
The program should return an integer, which is the minimum possible maximum sum of any subarray when the array arr is split into K subarrays.

Input :
4 3
1 2 3 4 


Output :
4


Constraints :
1 ≤ N ≤ 10^5
1 ≤ K ≤ N
1 ≤ arr[i] ≤ 10^5 
*/
#include<bits/stdc++.h>
using namespace std;
int main(){
    int n,k;
    cin>>n>>k;
    int arr[n];
    for(int i=0;i<n;i++)cin>>arr[i];
    int s=0,ans=0;
    for(int i=0;i<n;i++)
    {
        s+=arr[i];
        ans=max(ans,arr[i]);
    }
    if(k==1)cout<<s<<endl;
    else cout<<ans<<endl;
}
