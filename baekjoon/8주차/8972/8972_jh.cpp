#include <iostream>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
#define MAX 100

int R, C, inputJongsuMoveSize, playCnt = 0;
// 종수 아두이노의 위치와 각 좌표별 미친 아두이노 개수 저장
int jongsuArduinoX, jongsuArduinoY, crazyArduinoCnt[MAX][MAX];
// 미친 아두이노 위치 저장
queue<pair<int, int>> crazyArduino;
char MAP[MAX][MAX];
string inputJongsuMove;
// 종수 패배 여부 저장
bool lose;
int moveNum[10][2] = {{0, 0}, {1, -1}, {1, 0}, {1, 1}, {0, -1}, {0, 0}, {0, 1}, {-1, -1}, {-1, 0}, {-1, 1}};
// 종수 아두이노 이동
bool jongsuArduinoMove(int direction)
{
    int nextX = jongsuArduinoX + moveNum[direction][0];
    int nextY = jongsuArduinoY + moveNum[direction][1];
    playCnt++;
    // 종수 아두이노와 미친 아두이노가 만나면 종수 패배
    if (MAP[nextX][nextY] == 'R')
    {
        lose = true;
        return false;
    }
    else
    {
        // 현재 위치는 빈칸으로 남김
        MAP[jongsuArduinoX][jongsuArduinoY] = '.';
        // 종수 아두이노 이동
        MAP[nextX][nextY] = 'I';
        // 종수 아두이노 위치 업데이트
        jongsuArduinoX = nextX;
        jongsuArduinoY = nextY;
        return true;
    }
}
// 미친 아두이노들 이동
bool crazyArduinoMove()
{
    while (!crazyArduino.empty())
    {
        int currentX = crazyArduino.front().first;
        int currentY = crazyArduino.front().second;
        // 미친 아두이노와 종수 아두이노간의 최소 거리,
        // 미친 아두이노가 이동하게 될 위치 저장
        int minDistance = 200, nextX, nextY;
        crazyArduino.pop();
        for (int i = 1; i < 10; i++)
        {
            int tempNextX = currentX + moveNum[i][0];
            int tempNextY = currentY + moveNum[i][1];
            int distance = abs(jongsuArduinoX - tempNextX) + abs(jongsuArduinoY - tempNextY);
            if (minDistance > distance)
            {
                minDistance = distance;
                nextX = tempNextX;
                nextY = tempNextY;
            }
        }
        // 종수 아두이노와 미친 아두이노가 만나면 종수 패배
        if (MAP[nextX][nextY] == 'I')
        {
            lose = true;
            return false;
        }
        // 이동하려는 곳에 미친 아두이노가 있거나 빈칸이면
        if (MAP[nextX][nextY] == 'R' || MAP[nextX][nextY] == '.')
        {
            // 미친 아두이노 이동
            MAP[nextX][nextY] = 'R';
            // 이동하려는 위치의 미친 아두이노 개수 1 증가
            crazyArduinoCnt[nextX][nextY]++;
        }
        // 현재 위치의 미친 아두이노가 1개 미만이라면
        if (crazyArduinoCnt[currentX][currentY] <= 1)
        {
            // 현재 위치 빈칸으로 변경
            MAP[currentX][currentY] = '.';
        }
        // 현재 위치의 미친 아두이노 개수 1 감소
        crazyArduinoCnt[currentX][currentY]--;
    }
    return true;
}
// 같은 칸에 미친 아두이노가 2개 이상 있을 시 해당 칸 폭발시킴
void explosion()
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            // 현재 위치에 미친 아두이노가 1개 있다면
            if (crazyArduinoCnt[i][j] == 1)
            {
                // 미친 아두이노 위치 추가
                crazyArduino.push({i, j});
            }
            // 현재 위치에 미친 아두이노가 2개 이상 있다면
            else if (crazyArduinoCnt[i][j] >= 2)
            {
                // 현재 위치 빈칸으로 만듬
                MAP[i][j] = '.';
                // 현재 위치의 미친 아두이노 개수 0으로 변경
                crazyArduinoCnt[i][j] = 0;
            }
        }
    }
}

int main()
{
    cin >> R >> C;

    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            cin >> MAP[i][j];
            // 현재 위치에 미친 아두이노가 있다면
            if (MAP[i][j] == 'R')
            {
                // 미친 아두이노 위치 추가
                crazyArduino.push({i, j});
                // 현재 위치의 미친 아두이노 개수 1 증가
                crazyArduinoCnt[i][j]++;
            }
            // 현재 위치에 종수 아두이노가 있다면
            else if (MAP[i][j] == 'I')
            {
                // 위치 저장
                jongsuArduinoX = i;
                jongsuArduinoY = j;
            }
        }
    }

    cin >> inputJongsuMove;
    inputJongsuMoveSize = inputJongsuMove.size();

    for (int i = 0; i < inputJongsuMoveSize; i++)
    {
        // 이동 중간에 종수가 진다면 반복문 종료
        if (!jongsuArduinoMove(inputJongsuMove[i] - '0'))
        {
            break;
        }
        if (!crazyArduinoMove())
        {
            break;
        }
        explosion();
    }

    if (lose)
    {
        cout << "kraj " << playCnt;
    }
    else
    {
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                cout << MAP[i][j];
            }
            cout << '\n';
        }
    }

    return 0;
}