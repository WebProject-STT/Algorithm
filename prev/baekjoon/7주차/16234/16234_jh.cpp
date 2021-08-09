#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;
#define MAX 50
// 지도 정보와 각 연합국의 인구수를 저장하는 배열
int MAP[MAX][MAX], unionNum[MAX * MAX];
bool visited[MAX][MAX];
int moveNum[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
// 입력 변수와 연합 인구수와 칸의 개수, 연합국의 순서를 저장
int N, L, R, total = 0, cnt = 0, unionIndex = 0;
// 인구 이동 함수
void movePeople()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // 연합국의 인구수 갱신
            MAP[i][j] = unionNum[MAP[i][j]];
        }
    }
}
// 국경선을 여는 함수 (bfs를 재귀형태로 생성)
void openLine(int curX, int curY)
{
    visited[curX][curY] = true;

    for (int i = 0; i < 4; i++)
    {
        int nextX = curX + moveNum[i][0];
        int nextY = curY + moveNum[i][1];
        if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= N || visited[nextX][nextY])
        {
            continue;
        }
        int difference = abs(MAP[curX][curY] - MAP[nextX][nextY]);
        // 두 나라 간 인구 수 차이가 올바른 범위 내라면
        if (difference >= L && difference <= R)
        {
            // 현재 연합국 총 인구수 증가
            total += MAP[nextX][nextY];
            // 현재 연합국 수 증가
            cnt++;
            openLine(nextX, nextY);
        }
    }
    // 더이상 국경선을 공유하는 나라가 없다면 현재 좌표에 연합국의 인덱스를 저장
    MAP[curX][curY] = unionIndex;
}

int main()
{
    int answer = 0;
    cin >> N >> L >> R;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> MAP[i][j];
        }
    }

    while (1)
    {
        bool isOpenLine = false;
        unionIndex = 0;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (!visited[i][j])
                {
                    total = MAP[i][j];
                    cnt = 1;
                    openLine(i, j);
                    // 각 연합국의 인구수를 저장
                    unionNum[unionIndex++] = total / cnt;
                    // 인구 이동이 이뤄져야 한다면 isOpenLine true로 변경
                    if (cnt != 1)
                    {
                        isOpenLine = true;
                    }
                }
            }
        }
        // 인구 이동이 끝났다면 isOpenLine false로 변경
        if (!isOpenLine)
        {
            break;
        }
        // 인구 이동
        movePeople();
        memset(visited, false, sizeof(visited));
        answer++;
    }

    cout << answer;

    return 0;
}