/*
n=int(input())
a=list(map(int,input().split()))
k=n//2
if(n%2==0):
    k-=1
for i in range(n):
    if(i==k):
        continue
    else:
        print(a[i],end=" ")

*/
#include<bits/stdc++.h>
using namespace std;
void fun(stack<int>&s, int sizeOfStack)
    {
        // code here.. 
        vector<int>ve;
        while(!s.empty())
        {
            ve.push_back(s.top());
            s.pop();
        }
        reverse(ve.begin(),ve.end());
        int n=ve.size();
        int k=0;
        if(sizeOfStack%2==0) k=(n/2)-1;
        else k=(n/2);
        ve.erase(ve.begin()+k);
        for(int i=0;i<ve.size();i++)
        {
            s.push(ve[i]);
        }
    }
int main()
{
    int n;
    cin>>n;
    int arr[n];
    stack<int>st;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        st.push(arr[i]);
    }
    fun(st,n);
    vector<int>ve;
    while(!st.empty())
    {
        ve.push_back(st.top());
        st.pop();
    }
    reverse(ve.begin(),ve.end());
    for(auto it:ve) cout<<it<<" ";
}
