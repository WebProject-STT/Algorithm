#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int N, T, P, answer = 0;
	vector<pair<int, int>> input;
    // 최대 금액을 저장하는 벡터
    // maxProfit[i] => i번째 날에 받을 수 있는 최대 금액
    // 2일에 상담을 시작해서 3일에 끝난다면 3일에 돈을 받는다고 설정
	vector<int> maxProfit;

	cin >> N;
	input.resize(N + 1);
    // N번째 날에 하루 일하면 N+1번째 날에 돈을 받기 때문에 크기는 N+2(원소번호때문에 1 크게 설정)로 설정
	maxProfit.assign(N + 2, 0);

	for (int i = 0; i <= N; i++) {
		maxProfit[i] = 0;
	}

	for(int i = 1; i <= N; i++) {
		cin >> T >> P;
		input[i] = { T, P };
	}

	for (int i = 1; i <= N; i++) {
		int time = input[i].first;
		int profit = input[i].second;
        // i번째 날에 일을 했을 경우
		if (i + time <= N + 1) {
			maxProfit[i + time] = max(maxProfit[i + time], maxProfit[i] + profit);
		}
        // i번째 날에 일을 하지 않았을 경우
		maxProfit[i + 1] = max(maxProfit[i + 1], maxProfit[i]);
	}

	cout << maxProfit[N + 1];

	return 0;
}