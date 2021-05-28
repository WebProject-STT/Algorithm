#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    // 물건의 무게 저장
    vector<int> w;
    // 물건의 가치 저장
    vector<int> v;
    // 배낭에 넣을 수 있는 최대 가치 저장
    // => dp[i][j] = i번째 물건까지 확인하는데 물건의 무게 합이 j일 때, 최대 가치
    vector<vector<int>> dp;
    int N, K, x, y;

    cin >> N >> K;
    w.assign(N + 1, 0);
    v.assign(N + 1, 0);

    for (int i = 0; i <= N; i++)
    {
        if (i != 0)
            cin >> w[i] >> v[i];
        dp.push_back(vector<int>(K + 1, 0));
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= K; j++)
        {
            // 현재 물건의 무게, 이전 물건까지 확인 & j무게를 넣었을 때 최대 가치
            int currentWeight = w[i], previous = dp[i - 1][j];
            // j가 현재 무게보다 크거나 같다면
            // (이전 물건까지의 (j - 현재 물건의 무게)의 최대 가치 + 현재 물건 가치)와
            // (이전 물건까지의 현재 물건의 무게의 최대 가치) 중 큰 값이 dp[i][j]가 됨
            if (j >= w[i])
                dp[i][j] = max(dp[i - 1][j - currentWeight] + v[i], previous);
            // j가 현재 무게보다 작다면 previous를 대입
            else
                dp[i][j] = previous;
        }
    }

    cout << dp[N][K];
}