#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 100000

int main()
{
    int T, N;
    int *answer;

    cin >> T;
    answer = new int[T];

    for (int i = 0; i < T; i++)
    {
        int dp[2][MAX] = {0};
        int sticker[2][MAX];
        cin >> N;
        for (int k = 0; k < 2; k++)
        {
            for (int j = 0; j < N; j++)
            {
                cin >> sticker[k][j];
            }
        }
        dp[0][0] = sticker[0][0];
        dp[1][0] = sticker[1][0];
        dp[0][1] = dp[1][0] + sticker[0][1];
        dp[1][1] = dp[0][0] + sticker[1][1];
        for (int j = 2; j < N; j++)
        {
            // 메모리: 3456KB, 시간: 300ms
            dp[0][j] = sticker[0][j] + max(dp[1][j - 1], dp[1][j - 2]);
            dp[1][j] = sticker[1][j] + max(dp[0][j - 1], dp[0][j - 2]);
            /* 메모리: 3460KB, 시간: 296ms
            for (int k = 0; k < 2; k++) {
				dp[k][j] = sticker[k][j] + max(dp[-(k - 1)][j - 1], dp[-(k - 1)][j - 2]);
			}
            */
        }
        answer[i] = max(dp[0][N - 1], dp[1][N - 1]);
    }

    for (int i = 0; i < T; i++)
    {
        cout << answer[i] << '\n';
    }

    return 0;
}