#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    // 마실 수 있는 와인의 최대양과 와인의 양을 저장
    vector<int> dp, wine;

    cin >> n;
    dp.resize(n);
    wine.resize(n);

    for (int i = 0; i < n; i++)
    {
        cin >> wine[i];
    }
    // 첫번째 와인은 무조건 마심
    dp[0] = wine[0];
    // 첫번째, 두번째 와인은 무조건 마심
    dp[1] = wine[0] + wine[1];
    // (첫번째 + 두번째 와인), (첫 + 셋 와인) , (둘 + 셋 와인) 중 최대값
    dp[2] = max(dp[1], wine[2] + max(wine[0], wine[1]));

    for (int i = 3; i < n; i++)
    {
        // 와인을 마시는 경우의 수는 총 3가지 (연속으로 3잔 못먹음)
        // 1. 이전 와인을 마신 후에 현재 와인도 마신다 (연속 3잔 못 먹기 때문에 전전전 와인까지의 최대양을 더해야 함)
        //    => dp[i - 3] + wine[i - 1] + wine[i]
        // 2. 이전 와인을 건너 뛰고 현재 와인을 마신다
        //    => dp[i - 2] + wine[i]
        // 3. 현재 와인을 마시지 않는다
        // (현재 와인을 마심으로써 연속 3잔 못먹는다는 조건 때문에 올바른 최대값을 얻지 못할 수도 있음)
        //    => dp[i - 1]
        dp[i] = max(dp[i - 1], wine[i] + max(dp[i - 2], dp[i - 3] + wine[i - 1]));
    }

    cout << dp[n - 1];

    return 0;
}