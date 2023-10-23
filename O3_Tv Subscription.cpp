#include <iostream>
using namespace std;
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n,x;
        cin>>n>>x;
        int  s=(n/6)*(x);
        if (n % 6 != 0) {
            if (x<(n%6)*x) {
               s += x;
            } else {
              s+= (n% 6)*x;
            }
        }
        cout << s << endl;
    }

    return 0;
}
/*
Tv Subscription
Program Description :
A new TV streaming service was recently started in T-land called the Hub-TV.

A group of N friends in T-land want to buy Hub-TV subscriptions. We know that 6 people can share one Hub-TV subscription. Also, the cost of one Hub-TV subscription is X rupees. Determine the minimum total cost that the group of N friends will incur so that everyone in the group is able to use Hub-TV. 

Input Format :
The first line contains a single integer T the number of test cases. Then the test cases follow.

The first and only line of each test case contains two integers N and X — the size of the group of friends and the cost of one subscription. 

Output Format :
For each test case, output the minimum total cost that the group will incur so that everyone in the group is able to use Hub-TV.
 

Input :
3

1 100

12 250

16 135


Output :
100

500

405


Constraints :
1 <= T <= 1000

1 <= N <= 100

1 <= X <= 1000 
*/
