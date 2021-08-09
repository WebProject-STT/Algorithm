#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 100001
#define MOD 1000000009

int main()
{
    // dp[i][j] => 숫자 i를 1, 2, 3의 합으로 나타내는데 마지막을 j로 표현할 수 있는 경우의 수
    // 예) dp[4][1] => 1, 2, 1 / 3, 1 => 2
    long long dp[MAX][4];
    int *num;
    int T, maxNum;

    cin >> T;
    num = new int[T];

    for (int i = 0; i < T; i++)
    {
        cin >> num[i];
    }
    // dp 1, 2, 3번째 인덱스 초기화
    for (int i = 1; i < 4; i++)
    {
        for (int j = 1; j < 4; j++)
        {
            if (i == 3)
            {
                dp[i][j] = 1;
            }
            else
            {
                dp[i][j] = i == j ? 1 : 0;
            }
        }
    }
    // 입력값 중 최댓값 구함
    maxNum = *max_element(num, num + T);
    // 최댓값까지만 계산하도록 함
    for (int i = 4; i <= maxNum; i++)
    {
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD;
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD;
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD;
    }

    for (int i = 0; i < T; i++)
    {
        cout << (dp[num[i]][1] + dp[num[i]][2] + dp[num[i]][3]) % MOD << '\n';
    }
}