#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 50

int N, M;
// 맵 정보를 담은 배열
int MAP[MAX][MAX];
// 이동 가능한 경우의 수를 담은 배열
int moveNum[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int bfs(int x, int y)
{
    // 이동할 칸의 정보와 이동횟수를 담은 큐
    queue<vector<int>> need_visit;
    // 방문 정보를 담은 배열
    bool visited[MAX][MAX] = {false};
    need_visit.push({x, y, 0});
    visited[x][y] = true;

    while (!need_visit.empty())
    {
        int currentX = need_visit.front()[0];
        int currentY = need_visit.front()[1];
        int currentCnt = need_visit.front()[2];
        // 해당 칸에 상어가 있다면 이동횟수 반환
        if (MAP[currentX][currentY] == 1)
        {
            return currentCnt;
        }
        need_visit.pop();
        for (int i = 0; i < 8; i++)
        {
            int nextX = currentX + moveNum[i][0];
            int nextY = currentY + moveNum[i][1];
            if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M || visited[nextX][nextY])
            {
                continue;
            }
            need_visit.push({nextX, nextY, currentCnt + 1});
            visited[nextX][nextY] = true;
        }
    }
}

int main()
{
    int answer = 0;
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> MAP[i][j];
        }
    }

    // 모든 빈칸을 방문하며 bfs호출, 최댓값 탐색함
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (MAP[i][j] == 0)
            {
                answer = max(answer, bfs(i, j));
            }
        }
    }

    cout << answer;

    return 0;
}