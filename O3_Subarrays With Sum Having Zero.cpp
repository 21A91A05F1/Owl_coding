#include<bits/stdc++.h>
using namespace std;
int fun(int n,int arr[],int k)
{
    int c=0;
    for(int i=0;i<n;i++)
    {
        int s=0;
        for(int j=i;j<n;j++)
        {
            s+=arr[j];
            if(s==0)
            {
                c++;
            }
        }
    }
    return c++;
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    int k;
    cin>>k;
    int p=fun(n,arr,k);
    cout<<p;

}
