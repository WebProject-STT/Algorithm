#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
    1등, 1등, 2등, 2등 을 원할 경우
    1등, 2등, 3등, 4등 으로 만들어주는게 불만도가 제일 적은 방법
*/
int main() {
	vector<int> rank;
	long N, answer = 0;

	cin >> N;
	rank.resize(N + 1);

	for (int i = 1; i <= N; i++) {
		cin >> rank[i];
	}
    // 입력받은 등수 정렬
	sort(rank.begin(), rank.end());

	for (int i = 1; i <= N; i++) {
        // 현재 등수와 실제 등수(i)의 차이로 불만도 구함
        long dissatisfaction = abs(rank[i] - i);
        answer += dissatisfaction;
	}

	cout << answer;

	return 0;
}