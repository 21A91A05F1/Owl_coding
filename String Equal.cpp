/*
a = list(str(input()))
b = list(str(input()))
if len(a)!=len(b):
    print(0)
elif sorted(list(set(a)))==sorted(list(set(b))):
    print(1)
else:
    print(0)

*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s1,s2;
    cin>>s1>>s2;
    map<char,long long>mp1;
    map<char,long long>mp2;
    for(long long i=0;i<s1.size();i++) mp1[s1[i]]++;
    for(long long i=0;i<s2.size();i++) mp2[s2[i]]++;
    string a="",b="";
    vector<long long>ve1,ve2;
    for(auto it:mp1)
    {
        ve1.push_back(it.second);
        a+=it.first;
    }
    for(auto it:mp2)
    {
        ve2.push_back(it.second);
        b+=it.first;
    }
    sort(ve1.begin(),ve1.end());
    sort(ve2.begin(),ve2.end());
    long long f=0;
    for(long long i=0;i<ve1.size();i++)
    {
        if(ve1[i]!=ve2[i])
        {
            f=1;
            break;
        }
    }
    if(f==1) cout<<0;
    else
    {
        f=0;
        for(long long i=0;i<a.size();i++)
        {
              if(a[i]!=b[i])
              {
                f=1;
                break;
              }
        
        }
        if(f==1) cout<<0;
        else cout<<1;
    }
}
