#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 100000

int main() {
	int n, input, answer = 0;
	int num[MAX], dp[MAX];

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		num[i] = input;
	}
    // 수는 한 개 이상은 선택되야 하므로 dp[0]와 answer은 num[0]
	dp[0] = num[0];
	answer = num[0];

	for (int i = 1; i < n; i++) {
		int current = num[i];
        // 숫자들 연속해서 더한값과 현재값 중 최대값을 dp[i]에 대입
		dp[i] = max(dp[i - 1] + current, current);
        // 최대값 갱신
		answer = max(answer, dp[i]);
	}

	cout << answer;
	return 0;
}