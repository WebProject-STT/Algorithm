#include <iostream>
using namespace std;
#define MAX 1001
#define MOD 10007

int main()
{
    int n;
    int dp[MAX];

    cin >> n;

    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++)
    {
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
    }

    cout << dp[n] % MOD;

    return 0;
}