#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 16
int N;
int MAP[MAX][MAX];
int cnt = 0;
// 현재 위치와 방향을 매개변수로 받는 dfs 함수
void dfs(int x, int y, int dir)
{
    int nextX, nextY;
    // 현재 위치가 지도를 벗어나면 반환
    if (x >= N || y >= N)
    {
        return;
    }
    // 도착지에 도달했다면 cnt 증가시키고 반환
    if (x == N - 1 && y == N - 1)
    {
        cnt++;
        return;
    }
    // 대각선 방향으로 이동
    nextX = x + 1, nextY = y + 1;
    if (MAP[nextX - 1][nextY] != 1 && MAP[nextX][nextY - 1] != 1 && MAP[nextX][nextY] != 1)
    {
        dfs(nextX, nextY, 2);
    }
    // 현재 방향이 가로나 대각선일 경우
    if (dir == 0 || dir == 2)
    {
        // 가로 방향으로 이동
        nextX = x, nextY = y + 1;
        if (MAP[nextX][nextY] != 1)
        {
            dfs(nextX, nextY, 0);
        }
    }
    // 현재 방향이 세로나 대각선일 경우
    if (dir == 1 || dir == 2)
    {
        // 세로 방향으로 이동
        nextX = x + 1, nextY = y;
        if (MAP[nextX][nextY] != 1)
        {
            dfs(nextX, nextY, 1);
        }
    }
    return;
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> MAP[i][j];
        }
    }

    dfs(0, 1, 0);

    cout << cnt;

    return 0;
}