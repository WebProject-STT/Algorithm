#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 100
#define INF 1e9

int W, H;
char board[MAX][MAX];
// 거울 갯수 저장
int visited[MAX][MAX];
// 시작위치와 종료위치 저장
vector<pair<int, int>> target;
int moveNum[4][2] = { {-1, 0}, {0, -1}, {1, 0}, {0, 1} };

int bfs(int startX, int startY) {
	queue<vector<int>> needVisit;
    // 처음 시작할때는 어느 방향으로 가도 방향이 변경되지 않음
    // => 방향값을 -1로 넣음
	needVisit.push({ startX, startY, 0, -1 });
	visited[startX][startY] = 0;

	while (!needVisit.empty()) {
		int currentX = needVisit.front()[0];
		int currentY = needVisit.front()[1];
		int currentCnt = needVisit.front()[2];
		int currentDirection = needVisit.front()[3];
		needVisit.pop();
		for (int i = 0; i < 4; i++) {
			int nextX = currentX + moveNum[i][0];
			int nextY = currentY + moveNum[i][1];
            // 다음 위치까지 설치될 거울의 개수
			int nextCnt = currentCnt;
			if (nextX < 0 || nextX >= H || nextY < 0 || nextY >= W || board[nextX][nextY] == '*') {
				continue;
			}
            // 현재 방향과 다음방향이 같지 않고 시작위치가 아니라면
			if (currentDirection != i && currentDirection != -1) {
                // 방향이 변경되므로 nextCnt는 1 증가
				nextCnt++;
			}
            // 거울의 최소값을 구해야 하기 때문에
            // nextCnt가 현재 다음위치에 설치된 거울 개수보다 크다면 continue
			if (visited[nextX][nextY] < nextCnt) {
				continue;
			}
			visited[nextX][nextY] = nextCnt;
			needVisit.push({ nextX, nextY, nextCnt, i });
		}
	}
	return visited[target[1].first][target[1].second];
}

int main() {
	cin >> W >> H;
	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			cin >> board[i][j];
			if (board[i][j] == 'C') {
				target.push_back({ i, j });
			}
			visited[i][j] = INF;
		}
	}
	
	cout << bfs(target[0].first, target[0].second) << '\n';

	return 0;
}