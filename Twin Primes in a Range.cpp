#include<bits/stdc++.h>
using namespace std;
bool prime(int n){
    if(n<2) return false;
    if(n==2) return true;
    for(int i=2;i<sqrt(n)+1;i++) if(n%i==0) return false;
    return true;
}
int main(){
    int a, b;cin>>a>>b;
    for(int i=a;i<b-1;i++)
        if(prime(i) && prime(i+2)) cout<<i<<" "<<i+2<<endl;
}
