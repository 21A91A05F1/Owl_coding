#include <bits/stdc++.h> 
using namespace std;
void missingAndRepeating(vector<int> &arr, int n)
{
	int freq[n+1]={0};
	int a,b;
	for(int i=0;i<n;i++)
	{
		if(freq[arr[i]]==0) freq[arr[i]]++;
		else a=arr[i];
	}
	for(int i=1;i<n+1;i++) 
	{
		if(freq[i]==0) 
		{
			b=i;
		}
	}
	cout<<a<<" "<<b;
}
int main()
{
    int n;
    cin>>n;
    int arr[n];
    vector<int>ve;
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
        ve.push_back(arr[i]);
    }
    missingAndRepeating(ve,n);
}
