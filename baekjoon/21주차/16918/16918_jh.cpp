#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
/*
    0초 => 임의로 폭탄 설치
    1초 => 아무일도 일어나지 않음
    2초 => 폭탄 설치되지 않은 곳에 폭탄 설치
    3초 => 0초에 설치했던 폭탄 폭발시킴 (상하좌우에 설치된 폭탄 모두)
    4초 => 폭탄 설치되지 않은 곳에 폭탄 설치
    5초 => 2초에 설치했던 폭탄 폭발시킴 (상하좌우에 설치된 폭탄 모두)
    ...
*/
// 격자판 상태 저장 (-1은 아무것도 설치안됨, 0이상은 폭탄이 설치된 시간 의미)
vector<vector<int>> MAP;
// 입력값과 현재시간 저장, 봄버맨은 1초동안 아무것도 안하기 때문에 현재시간 초기값은 1
int R, C, N, currentTime = 1;
int moveNum[4][2] = { {-1, 0}, {0, -1}, {1, 0}, {0, 1} };
// 폭탄 설치
void installBomb() {
	currentTime++;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
            // 폭탄 설치안돼있으면 설치
			if (MAP[i][j] == -1) {
				MAP[i][j] = currentTime;
			}
		}
	}
}
// 폭탄 폭발
void explodeBomb() {
    // 현재 시간으로부터 3초 전에 설치된 폭탄 위치 저장
	queue<pair<int, int>> bombLocation;
	currentTime++;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (currentTime - MAP[i][j] == 3) {
				bombLocation.push({ i, j });
                // 폭탄 폭발
				MAP[i][j] = -1;
			}
		}
	}
	while (!bombLocation.empty()) {
		int currentX = bombLocation.front().first;
		int currentY = bombLocation.front().second;
		bombLocation.pop();
		for (int k = 0; k < 4; k++) {
			int nextX = currentX + moveNum[k][0];
			int nextY = currentY + moveNum[k][1];
			if (nextX < 0 || nextX >= R || nextY < 0 || nextY >= C || MAP[nextX][nextY] == -1) {
				continue;
			}
			MAP[nextX][nextY] = -1;
		}
	}
}

int main() {
	char input;
	int repeatCnt;
	bool remain;

	cin >> R >> C >> N;
	MAP.assign(R, vector<int>(C, -1));

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> input;
			if (input == 'O') {
				MAP[i][j] = 0;
			}
		}
	}
    // 폭탄 설치 및 폭발 반복 횟수
	repeatCnt = (N - 1) / 2;
    // N의 홀수 여부
	remain = (N - 1) % 2 != 0 ? true : false;

	for(int i = 0; i < repeatCnt; i++) {
		installBomb();
		explodeBomb();
	}
    // remain이 true이면 폭탄 한번 더 설치해야함
	if (remain) {
		installBomb();
	}

	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (MAP[i][j] == -1) {
				cout << ".";
			}
			else {
				cout << "O";
			}
		}
		cout << '\n';
	}
	
	return 0;
}