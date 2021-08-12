#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    unsigned long long int n, d;
    cin >> n >> d;

    cout.precision(34);
    while(n!=0 || d!=0){
        cout << pow(n,d) << endl;
        cin >> n >> d;
    }

    return 0;
}