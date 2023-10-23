#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        //cout<<n<<k;
        int arr[n];
        k=k%n;
        vector<int>ve;
        for(int i=0;i<n;i++) 
        {
            cin>>arr[i];
            ve.push_back(arr[i]);
        }
        reverse(ve.begin(),ve.end());
        reverse(ve.begin(),ve.begin()+k);
        reverse(ve.begin()+k,ve.end());
        for(int i=0;i<n;i++)
        {
            if(i==n-1) cout<<ve[i];
            else cout<<ve[i]<<" ";
        }
        cout<<endl;
    }
}
