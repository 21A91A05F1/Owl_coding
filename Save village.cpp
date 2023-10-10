/*
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(i+1,n):
        if l[j]>l[i]:
            c+=l[j]
            break
print(c%1000000001)
*/
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
