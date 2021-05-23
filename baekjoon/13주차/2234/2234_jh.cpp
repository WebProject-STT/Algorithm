#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 50

int N, M;
// 각 칸의 성곽 정보, 방 번호 및 현재 방의 개수 저장하는 배열과 변수
int castle[MAX][MAX], roomNum[MAX][MAX], currentRoomNum = 0;
// 서, 북, 동, 남 방향
int moveNum[4][2] = { {0, -1}, {-1, 0}, {0, 1}, {1, 0} };
bool visited[MAX][MAX];
// 방의 넓이 저장
vector<int> area;
// 방의 총 개수와 각 방의 넓이를 bfs로 구함
int bfs(int startX, int startY) {
	int roomArea = 1;
	queue<pair<int, int>> needVisit;
	needVisit.push({ startX, startY });
	visited[startX][startY] = true;
	roomNum[startX][startY] = currentRoomNum;
	while (!needVisit.empty()) {
		int currentX = needVisit.front().first;
		int currentY = needVisit.front().second;
        // 성곽 정보
		int currentInfo = castle[currentX][currentY];
		int directionNum = 0;
		vector<int> moveDirection;
		needVisit.pop();
        // 성곽 정보를 이진수로 변경해 어느 쪽이 뚫려 있는지 확인
		while (directionNum < 4) {
            // 뚫려있는 쪽을 발견하면 moveDirection에 해당 방향 추가
			if ((currentInfo % 2) == 0) {
				moveDirection.push_back(directionNum);
			}
			directionNum++;
			currentInfo /= 2;
		}
        // 이동가능한 방향으로 이동
		for (auto elem : moveDirection) {
			int nextX = currentX + moveNum[elem][0];
			int nextY = currentY + moveNum[elem][1];
			if (!visited[nextX][nextY]) {
				visited[nextX][nextY] = true;
				needVisit.push({ nextX, nextY });
                // 방 번호 표시
				roomNum[nextX][nextY] = currentRoomNum;
				roomArea++;
			}
		}
	}
	currentRoomNum++;
    // 해당 방의 넓이 반환
	return roomArea;
}
// 벽 하나 제거했을때 얻을 수 있는 가장 넓은 방 크기 구하기
int removeWall() {
	int maxArea = 0;
    // 두 방의 넓이를 계산했는지 확인하기 위한 벡터
	vector<vector<bool>> check;
	check.assign(currentRoomNum, vector<bool>(currentRoomNum, false));
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			int currentNum = roomNum[i][j];
            // 현재 방에서 상하좌우에 있는 방의 번호를 확인
			for (int k = 0; k < 4; k++) {
				int nextX = i + moveNum[k][0];
				int nextY = j + moveNum[k][1];
				int nextNum = roomNum[nextX][nextY];
				if (nextX < 0 || nextX >= M || nextY < 0 || nextY >= N) {
					continue;
				}
                // 현재 방과 이웃한 방이 번호가 다르고 아직 확인하지 않은 경우라면
				if (currentNum != nextNum && !check[currentNum][nextNum]) {
					check[currentNum][nextNum] = true;
					check[nextNum][currentNum] = true;
                    // maxArea 갱신
					maxArea = max(maxArea, area[currentNum] + area[nextNum]);
				}
			}
		}
	}
    // 가장 넓은 방 크기 반환
	return maxArea;
}

int main() {
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			cin >> castle[i][j];
		}
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			roomNum[i][j] = -1;
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
            // 방을 아직 탐색하지 않았다면
			if (roomNum[i][j] == -1) {
                // 해당 방의 넓이를 구해서 area에 삽입
				area.push_back(bfs(i, j));
			}
		}
	}
	cout << currentRoomNum << '\n';
	cout << *max_element(area.begin(), area.end()) << '\n';
	cout << removeWall();
	return 0;
}