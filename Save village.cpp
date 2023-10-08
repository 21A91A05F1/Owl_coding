#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++)cin>>arr[i];
    stack<long>q;
    long long ans=0;
    for(int i=n-1;i>=0;i--)
    {
        while(!q.empty() and arr[i]>=q.top())q.pop();
        if(!q.empty())ans+=q.top();
        ans=ans%1000000001;
        q.push(arr[i]);
    }
    cout<<ans% 1000000001<<endl;
}
