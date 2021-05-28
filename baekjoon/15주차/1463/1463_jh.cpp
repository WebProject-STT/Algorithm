#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N;
  // dp[i] => i를 1로 만드는데 필요한 연산 최소 횟수
	vector<int> dp;
	
	cin >> N;
	dp.resize(N + 1);
  // 1은 이미 1이므로 연산 필요없음
	dp[1] = 0;
  // 낮은 숫자에서 N까지 올라가며 더함
	for (int i = 2; i <= N; i++) {
    // 모든 숫자는 1을 빼는 연산이 가능함
    // => dp[i]에 i-1의 최소 횟수에 1을 더한 값을 대입
		dp[i] = dp[i - 1] + 1;
    // i가 3으로 나눠지면 i/3의 최소 횟수에 1을 더한 값과 dp[i] 중 최소값 대입
		if (i % 3 == 0) {
			dp[i] = min(dp[i], dp[i / 3] + 1);
		}
    // i가 2로 나눠지면 i/2의 최소 횟수에 1을 더한 값과 dp[i] 중 최소값 대입
		if (i % 2 == 0) {
			dp[i] = min(dp[i], dp[i / 2] + 1);
		}
	}

	cout << dp[N];

	return 0;
}