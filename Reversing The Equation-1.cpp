#include<bits/stdc++.h>
using namespace std;
int main(){
    string str1;
    cin>>str1;
    string ans="";
    string temp="";
    for(int i=str1.length()-1;i>=0;i--){
        if(str1[i]>='0'&&str1[i]<='9'){
        temp=str1[i]+temp;
        }
        else{
            if(!temp.empty()){
                ans+=temp+str1[i];
                temp="";
            }
            else
                ans+=str1[i];
    }
    }
    if(!temp.empty()){
        ans+=temp;
    }
    cout<<ans<<endl;
}
