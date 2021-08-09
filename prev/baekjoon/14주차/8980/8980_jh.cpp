#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 100

struct deliver {
	int sender;
	int receiver;
	int cnt;
};
/*
    물건을 많이 배송하기 위해선
    1번과 가까운 마을부터 배송해야 한다
    중간중간에 마을에 박스 배송하고 다시 실으면서
    배송 개수를 늘릴 수 있는데
    멀리 가는 마을의 박스를 먼저 실게 되면
    용량제한으로 배송을 많이 할 수 없음
*/
bool cmp(deliver &a, deliver &b) {
	if (a.receiver == b.receiver) {
		return a.sender < b.sender;
	}
	return a.receiver < b.receiver;
}

int main() {
	int N, C, M, answer = 0;
    // 입력값 관리 벡터
	vector<deliver> input;
    // 각 마을에서 트럭에 실고 있는 택배 박스의 최대 개수
	vector<int> capacity;

	cin >> N >> C;
	cin >> M;
	input.resize(M);
	capacity.assign(N + 1, 0);

	for (int i = 0; i < M; i++) {
		cin >> input[i].sender >> input[i].receiver >> input[i].cnt;
	}
    
	sort(input.begin(), input.end(), cmp);

	for (int i = 0; i < M; i++) {
		int sender = input[i].sender;
		int receiver = input[i].receiver;
		int cnt = input[i].cnt;
        // 출발 마을부터 도착 마을 전까지 확인하며 배송가능한 택배 개수 구함
        // (도착 마을에서는 택배를 배송해서 개수가 줄기 때문에 전까지만 확인하면 됨)
		for (int j = sender; j < receiver; j++) {
            // 해당 마을에서 트럭 용량이 꽉 차서 택배를 실을 수 없거나 일부만 실을 수 있다면
            if(cnt + capacity[j] > C) {
                // 실을 수 있는 택배 개수 변경
				cnt = C - capacity[j];
			}
		}
        // 최종으로 실을 수 있는 택배 개수 쭉 더해줌
        for (int j = sender; j < receiver; j++) {
			capacity[j] += cnt;
		}
        // 정답에 최종적으로 이번에 실은 택배 개수 더해줌 => 택배를 실었다는건 언젠가 배송될거라는 의미
		answer += cnt;
	}
	cout << answer;

	return 0;
}