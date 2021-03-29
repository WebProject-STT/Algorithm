#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 101

bool MAP[MAX][MAX], visited[MAX][MAX];
int moveNum[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
int N, M, K;
// 정말 전형적인 bfs 문제
int bfs(int startX, int startY)
{
    int cnt = 1;
    queue<pair<int, int>> needVisit;
    needVisit.push({startX, startY});

    while (!needVisit.empty())
    {
        int currentX = needVisit.front().first;
        int currentY = needVisit.front().second;
        needVisit.pop();
        for (int i = 0; i < 4; i++)
        {
            int nextX = currentX + moveNum[i][0];
            int nextY = currentY + moveNum[i][1];
            if (nextX <= 0 || nextX > N || nextY <= 0 || nextY > M || visited[nextX][nextY] || !MAP[nextX][nextY])
            {
                continue;
            }
            visited[nextX][nextY] = true;
            needVisit.push({nextX, nextY});
            cnt++;
        }
    }
    return cnt;
}

int main()
{
    int size = 0;
    cin >> N >> M >> K;

    for (int i = 0; i < K; i++)
    {
        int r, c;
        cin >> r >> c;
        MAP[r][c] = true;
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            if (MAP[i][j])
            {
                visited[i][j] = true;
                size = max(size, bfs(i, j));
            }
        }
    }

    cout << size;

    return 0;
}