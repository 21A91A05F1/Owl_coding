#include<bits/stdc++.h>
using namespace std;
int main(){
    string s1,s2;
    cin>>s1>>s2;
    string s3;
    for(int i=0;i<s2.size();i++){
        if(s2[i]!=s2[i+1]){
            s3+=s2[i];
        }
    }
    if(s3==s1){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
}
