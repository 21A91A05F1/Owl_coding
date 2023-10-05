#include <iostream>
#include <vector>
using namespace std;
int sum_of_digits(int num) {
    int sum = 0;
    while (num !=0) {
        sum += num % 10;
        num /= 10;
    }
    return sum;
}
vector<int> prime_factors(int n) {
    vector<int> ve;
    int i= 2;
    while (n> 1) {
        while (n % i == 0) {
            ve.push_back(i);
            n/=i;
        }
        i+=1;
    }
    return ve;
}
int is_super_number(int n) {
    int so = sum_of_digits(n);
    vector<int> fac = prime_factors(n);
    int s = 0;
    for (int it : fac) {
        s += sum_of_digits(it);
    }
    if(so==s) return 1;
    return 0;
}

int main() {
    int n;
    cin >> n;
    cout << is_super_number(n) << endl;
    return 0;
}
