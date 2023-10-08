#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    int n=s.size();
    vector<vector<int>>ve(5,vector<int>(s.size(),0));
    for(int i=0;i<s.size();i++)
    {
        int g=1;
        int l=s[i]-'0';
        if(l>=5) 
        {
            ve[0][i]=1;
            l-=5;
        }
        while(l>0)
        {
            ve[g][i]=1;
            l--;
            g++;
        }
    }
    for(int i=0;i<5;i++)
    {
        for(int j=0;j<s.size();j++)
        {
           if(j==n-1) cout<<ve[i][j];
           else cout<<ve[i][j]<<" ";
        }
        cout<<endl;
    }
}
