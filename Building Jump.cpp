#include <bits/stdc++.h>
using namespace std;
int fun(int arr[], int n)
{
	int c=0,m=0;
	for (int i=1;i<n;i++) {
		if (arr[i] > arr[i - 1])
			c++;
		else {
			m = max(m,c);
			c=0;
		}
	}
	return max(m,c);
}
int main()
{
	int n;
	cin>>n;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
	cout << fun(arr, n);
}
