#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 8

int N, M, answer = 0;
int moveNum[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// 원래 지도, 벽 세울때 사용할 지도, 바이러스 퍼트릴때 사용할 지도
int MAP[MAX][MAX], tempMAP[MAX][MAX], changeMAP[MAX][MAX];
// 바이러스 위치 저장하는 벡터
vector<pair<int, int>> virusPosition;
// 배열 복사
void copy(int (*a)[8], int (*b)[8])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            a[i][j] = b[i][j];
        }
    }
}
// 안전 영역의 최대 크기를 answer 변수에 저장
void getSize()
{
    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (changeMAP[i][j] == 0)
            {
                cnt++;
            }
        }
    }
    answer = max(answer, cnt);
    return;
}
// 바이러스 퍼뜨리기
void bfs()
{
    queue<pair<int, int>> needVisit;
    // 바이러스 위치를 큐에 넣음
    for (auto elem : virusPosition)
    {
        needVisit.push({elem.first, elem.second});
    }
    copy(changeMAP, tempMAP);
    while (!needVisit.empty())
    {
        int currentX = needVisit.front().first;
        int currentY = needVisit.front().second;
        needVisit.pop();
        for (int i = 0; i < 4; i++)
        {
            int nextX = currentX + moveNum[i][0];
            int nextY = currentY + moveNum[i][1];
            if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= M)
            {
                continue;
            }
            if (changeMAP[nextX][nextY] == 0)
            {
                changeMAP[nextX][nextY] = 2;
                needVisit.push({nextX, nextY});
            }
        }
    }
}
// dfs로 벽 세움
void makeWall(int cnt)
{
    if (cnt == 3)
    {
        bfs();
        getSize();
        return;
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (tempMAP[i][j] == 0)
            {
                tempMAP[i][j] = 1;
                makeWall(cnt + 1);
                tempMAP[i][j] = 0;
            }
        }
    }
    return;
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> MAP[i][j];
            // 바이러스 위치 저장
            if (MAP[i][j] == 2)
            {
                virusPosition.push_back({i, j});
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (MAP[i][j] == 0)
            {
                copy(tempMAP, MAP);
                tempMAP[i][j] = 1;
                makeWall(1);
                tempMAP[i][j] = 0;
            }
        }
    }

    cout << answer;

    return 0;
}