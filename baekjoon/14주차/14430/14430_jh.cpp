#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 300

int main() {
	int N, M;
    // 자원 정보와 dp배열 선언
	int MAP[MAX][MAX], dp[MAX][MAX];

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> MAP[i][j];
		}
	}
    // dp배열 초기화
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			dp[i][j] = 0;
		}
	}
    // (0, 0)에서 수집할 수 있는 최대 광석의 개수는 MAP[0][0]
    // => dp[0][0]은 MAP[0][0]으로 초기화
	dp[0][0] = MAP[0][0];
    // 각 칸을 모두 검사
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
            // i가 마지막 행이 아닐 경우
            // 현재 칸에서 아래로 이동할 수 있음
			if (i != N - 1) {
                // (i + 1, j)까지 왔을 때 수집할 수 있는 광석의 개수 (경로로 따짐)
                //  1. (i, j)에서 아래로 내려옴 => dp[i][j] + MAP[i + 1][j]
                //  2. 다른 경로에서 온 값 => dp[i + 1][j] => 이미 저장되있음
                //  둘 중에 최대값을 선정
				dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + MAP[i + 1][j]);
			}
            // j가 마지막 열이 아닐 경우
            // 현재 칸에서 오른쪽으로 이동할 수 있음
			if (j != M - 1) {
                // (i, j + 1)까지 왔을 때 수집할 수 있는 광석의 개수 (경로로 따짐)
                //  1. (i, j)에서 오른쪽으로 이동 => dp[i][j] + MAP[i][j + 1]
                //  2. 다른 경로에서 온 값 => dp[i][j + 1] => 이미 저장되있음
                //  둘 중에 최대값을 선정
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + MAP[i][j + 1]);
			}
		}
	}

	cout << dp[N - 1][M - 1];

	return 0;
}