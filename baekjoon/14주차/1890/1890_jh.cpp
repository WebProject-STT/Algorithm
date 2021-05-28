#include <iostream>
using namespace std;
#define MAX 100

int main() {
	int N;
	int gameMap[MAX][MAX];
    // 경로 개수가 최대 2^63-1까지 나올 수 있기 때문에 long long형으로 선언해야됨
	long long dp[MAX][MAX];

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> gameMap[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			dp[i][j] = 0;
		}
	}

	dp[0][0] = 1;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int current = gameMap[i][j];
            // 현재 칸에 이동경로가 없다면 continue 
			if (current < 1) {
				continue;
			}
            // 칸에 적힌 숫자만큼 오른쪽으로 이동할 수 있다면
			if (i + current < N) {
                // 경로 개수 증가
				dp[i + current][j] += dp[i][j];
			}
            // 칸에 적힌 숫자만큼 아래로 이동할 수 있다면
			if (j + current < N) {
                // 경로 개수 증가
				dp[i][j + current] += dp[i][j];
			}
		}
	}

	cout << dp[N - 1][N - 1];

	return 0;
}