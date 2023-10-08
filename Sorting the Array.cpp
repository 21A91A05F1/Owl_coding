#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int>ve1(n);
    vector<int>ve2(n);
    for(int i=0;i<n;i++) 
    {
        cin>>ve1[i];
        ve2[i]=ve1[i];
    }
    sort(ve2.begin(),ve2.end());
    if(ve1==ve2)
    {
        cout<<"yes"<<endl;
        cout<<"1 1"<<endl;
    }
    else
    {
        int l=0;
        while(ve1[l]==ve2[l]) l++;
        int r=n-1;
        while(ve1[r]==ve2[r]) r--;
        reverse(ve1.begin()+l,ve1.begin()+r+1);
        if(ve1==ve2) 
        {
            cout<<"yes"<<endl;
            cout<<l+1<<" "<<r+1<<endl;
        }
        else 
        {
            cout<<"no"<<endl;
        }
    }

}
