#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#define MAX 20
using namespace std;
int N, answer = 0;
int MAP[MAX][MAX];
// 블록의 숫자들을 저장할 큐
queue<int> num;
// 배열 복사
void copy(int arr[MAX][MAX], int arr2[MAX][MAX])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            arr2[i][j] = arr[i][j];
        }
    }
}
// 전체 블록 위로 이동
void up()
{
    for (int j = 0; j < N; j++)
    {
        // 블록을 놓을 위치
        int idx = 0;
        for (int i = 0; i < N; i++)
        {
            // 블록 발견하면 큐에 블록 숫자 추가
            if (MAP[i][j] != 0)
            {
                num.push(MAP[i][j]);
                // 해당 위치의 숫자는 0으로 변경
                MAP[i][j] = 0;
            }
        }
        while (!num.empty())
        {
            int current = num.front();
            num.pop();
            // 블록 놓으려는 곳이 비어있다면
            if (MAP[idx][j] == 0)
            {
                // 블록 위로 이동
                MAP[idx][j] = current;
            }
            // 블록 놓으려는 곳에 같은 숫자의 블록이 있다면
            else if (MAP[idx][j] == current)
            {
                // 해당 블록 숫자 2배 증가시키고 인덱스 증가
                MAP[idx++][j] *= 2;
            }
            // 블록 놓으려는 곳에 다른 숫자의 블록이 있다면
            else
            {
                // 인덱스 증가시켜서 해당 블록 밑에 놓음
                MAP[++idx][j] = current;
            }
        }
    }
}
// 전체 블록 아래로 이동
// (열과 헹 번호만 다를뿐, up함수와 로직 똑같음)
void down()
{
    for (int j = 0; j < N; j++)
    {
        int idx = N - 1;
        for (int i = N - 1; i >= 0; i--)
        {
            if (MAP[i][j] != 0)
            {
                num.push(MAP[i][j]);
                MAP[i][j] = 0;
            }
        }
        while (!num.empty())
        {
            int current = num.front();
            num.pop();
            if (MAP[idx][j] == 0)
            {
                MAP[idx][j] = current;
            }
            else if (MAP[idx][j] == current)
            {
                MAP[idx--][j] *= 2;
            }
            else
            {
                MAP[--idx][j] = current;
            }
        }
    }
}
// 전체 블록 왼쪽으로 이동
void left()
{
    for (int i = 0; i < N; i++)
    {
        int idx = 0;
        for (int j = 0; j < N; j++)
        {
            if (MAP[i][j] != 0)
            {
                num.push(MAP[i][j]);
                MAP[i][j] = 0;
            }
        }
        while (!num.empty())
        {
            int current = num.front();
            num.pop();
            if (MAP[i][idx] == 0)
            {
                MAP[i][idx] = current;
            }
            else if (MAP[i][idx] == current)
            {
                MAP[i][idx++] *= 2;
            }
            else
            {
                MAP[i][++idx] = current;
            }
        }
    }
}
// 전체 블록 오른쪽으로 이동
void right()
{
    for (int i = 0; i < N; i++)
    {
        int idx = N - 1;
        for (int j = N - 1; j >= 0; j--)
        {
            if (MAP[i][j] != 0)
            {
                num.push(MAP[i][j]);
                MAP[i][j] = 0;
            }
        }
        while (!num.empty())
        {
            int current = num.front();
            num.pop();
            if (MAP[i][idx] == 0)
            {
                MAP[i][idx] = current;
            }
            else if (MAP[i][idx] == current)
            {
                MAP[i][idx--] *= 2;
            }
            else
            {
                MAP[i][--idx] = current;
            }
        }
    }
}
// dfs로 완전탐색 수행
void dfs(int cnt)
{
    int MAP_copy[MAX][MAX];
    // 5번 이동하면 가장 큰 블록의 값 구함
    if (cnt == 5)
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                answer = max(answer, MAP[i][j]);
            }
        }
        return;
    }
    // 원래 보드 상태를 임시 배열에 복사해놓음
    copy(MAP, MAP_copy);

    for (int i = 0; i < 4; i++)
    {
        // 전체 블록을 상하좌우로 이동
        if (i == 0)
        {
            up();
        }
        else if (i == 1)
        {
            down();
        }
        else if (i == 2)
        {
            left();
        }
        else
        {
            right();
        }
        dfs(cnt + 1);
        // 임시 배열 상태를 보드에 저장
        copy(MAP_copy, MAP);
    }
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

    dfs(0);

    cout << answer;

    return 0;
}
