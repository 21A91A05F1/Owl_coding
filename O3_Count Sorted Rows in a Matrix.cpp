#include<bits/stdc++.h>
using namespace std;
bool is_revsorted(vector<int>ve)
{
    vector<int>sorted_ve=ve;
    sort(sorted_ve.begin(),sorted_ve.end());
    reverse(sorted_ve.begin(),sorted_ve.end());
    return sorted_ve==ve;
}
bool is_sorted(vector<int>ve)
{
    vector<int>sorted_ve=ve;
    sort(sorted_ve.begin(),sorted_ve.end());
    return sorted_ve==ve;
}
int main()
{
    int n,m;
    cin>>n>>m;
    int arr[n][m];
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>arr[i][j];
        }
    }
    int c=0;
    for(int i=0;i<n;i++)
    {
        vector<int>ve;
        for(int j=0;j<m;j++)
        {
            ve.push_back(arr[i][j]);
        }
        if(is_sorted(ve) or is_revsorted(ve)) c++;
    }
    cout<<c;
}
