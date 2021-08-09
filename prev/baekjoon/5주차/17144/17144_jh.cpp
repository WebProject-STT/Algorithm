#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 50
// 시간이 좀 오래 걸리는데 맵을 복사하면 시간 줄어들 거 같음!! 귀찮아서 시도는 안 해봄
int R, C, T;
int MAP[MAX][MAX];
// 미세먼지 위치와 양을 저장
queue<vector<int>> dust;
// 공기청정기의 x좌표 저장
vector<int> airCleaner;
int moveNum[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// 미세먼지 위치와 양을 큐에 넣음
void addDust()
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (MAP[i][j] > 0)
            {
                dust.push({i, j, MAP[i][j]});
            }
        }
    }
}
// 미세먼지 확산
void spreadDust()
{
    while (!dust.empty())
    {
        int currentX = dust.front()[0];
        int currentY = dust.front()[1];
        int currentDust = dust.front()[2];
        dust.pop();
        for (int i = 0; i < 4; i++)
        {
            int nextX = currentX + moveNum[i][0];
            int nextY = currentY + moveNum[i][1];
            if (nextX < 0 || nextX >= R || nextY < 0 || nextY >= C)
            {
                continue;
            }
            if ((nextX == airCleaner[0] && nextY == 0) || (nextX == airCleaner[1] && nextY == 0))
            {
                continue;
            }
            MAP[nextX][nextY] += currentDust / 5;
            MAP[currentX][currentY] -= currentDust / 5;
        }
    }
}
// 위쪽 공기청정기 작동
void cleanTopAir()
{
    int startX = airCleaner[0];
    for (int i = startX - 1; i > 0; i--)
    {
        MAP[i][0] = MAP[i - 1][0];
    }
    for (int j = 0; j < C - 1; j++)
    {
        MAP[0][j] = MAP[0][j + 1];
    }
    for (int i = 0; i < startX; i++)
    {
        MAP[i][C - 1] = MAP[i + 1][C - 1];
    }
    for (int j = C - 1; j > 1; j--)
    {
        MAP[startX][j] = MAP[startX][j - 1];
    }
    MAP[startX][1] = 0;
}
// 아래쪽 공기청정기 작동
void cleanBottomAir()
{
    int startX = airCleaner[1];
    for (int i = startX + 1; i < R - 1; i++)
    {
        MAP[i][0] = MAP[i + 1][0];
    }
    for (int j = 0; j < C - 1; j++)
    {
        MAP[R - 1][j] = MAP[R - 1][j + 1];
    }
    for (int i = R - 1; i > startX; i--)
    {
        MAP[i][C - 1] = MAP[i - 1][C - 1];
    }
    for (int j = C - 1; j > 1; j--)
    {
        MAP[startX][j] = MAP[startX][j - 1];
    }
    MAP[startX][1] = 0;
}

int main()
{
    int answer = 0;
    cin >> R >> C >> T;

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cin >> MAP[i][j];
            if (MAP[i][j] == -1)
            {
                airCleaner.push_back(i);
            }
        }
    }

    for (int i = 0; i < T; i++)
    {
        addDust();
        spreadDust();
        cleanTopAir();
        cleanBottomAir();
    }
    // 먼지 양 합산
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (MAP[i][j] > 0)
            {
                answer += MAP[i][j];
            }
        }
    }

    cout << answer;

    return 0;
}