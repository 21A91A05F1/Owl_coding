#include<iostream>
using namespace std;
int PalinArray(int a[], int n)
{
    for( int i = 0 ; i< n ; i++){
        int num  = a[i];
        int rev = 0 ; 
        while( num!=0 ){
            int d=num%10;
            rev = rev *10 + d;
            num/= 10;    
            }      
            if(rev!=a[i]){
             return 0; 
            }
    }
    return 1;      

}  
int main()        
{
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    cout<<PalinArray(arr,n);
}
