#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int fun(vector<int>& arr) {
    unordered_set<int> s;
    int c = 0;
    for (int i : arr) {
        //cout<<s.count(i)<<" ";
        while (s.count(i)) {
            i++;
            c++;
        }
        s.insert(i);
    }
    return c;
}

int main() {
    int n;
    cin >> n;
    vector<int>arr(n);
    for (int i = 0; i < n; i++) cin>>arr[i];
    cout<<fun(arr);

   
}
