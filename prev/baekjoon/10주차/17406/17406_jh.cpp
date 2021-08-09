#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define INF 1e9
#define MAX 51

int N, M, K, answer = INF;
int A[MAX][MAX];
vector<vector<int>> operation;
vector<bool> visited;

void copy(int A[][MAX], int B[][MAX])
{
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            B[i][j] = A[i][j];
        }
    }
}

int getMinValue()
{
    int minValue = INF;
    for (int i = 1; i <= N; i++)
    {
        int total = 0;
        for (int j = 1; j <= M; j++)
        {
            total += A[i][j];
        }
        minValue = min(minValue, total);
    }
    return minValue;
}
// 배열 돌리는 함수
void rotation(int current)
{
    int r = operation[current][0];
    int c = operation[current][1];
    int s = operation[current][2];
    int add = 2 * s;
    int startX = r - s, startY = c - s;

    while (add > 0)
    {
        int previous = A[startX][startY];
        // 오른쪽으로 이동
        for (int j = startY + 1; j <= startY + add; j++)
        {
            int current = A[startX][j];
            A[startX][j] = previous;
            previous = current;
        }
        // 아래쪽으로 이동
        for (int i = startX + 1; i <= startX + add; i++)
        {
            int current = A[i][startY + add];
            A[i][startY + add] = previous;
            previous = current;
        }
        // 왼쪽으로 이동
        for (int j = startY + add - 1; j >= startY; j--)
        {
            int current = A[startX + add][j];
            A[startX + add][j] = previous;
            previous = current;
        }
        // 위쪽으로 이동
        for (int i = startX + add - 1; i >= startX; i--)
        {
            int current = A[i][startY];
            A[i][startY] = previous;
            previous = current;
        }
        // 한바퀴 돌때마다 회전 시작 위치의 X, Y좌표는 1씩 증가
        startX++;
        startY++;
        // 한번 이동(왼 OR 오 OR 아 OR 위)할때 확인하는 칸의 개수는 2씩 줄어듬
        add -= 2;
    }
}
// 연산 순서 조합
void dfs(int current, int cnt)
{
    int B[MAX][MAX];
    if (cnt > 0)
    {
        rotation(current);
    }
    if (cnt == K)
    {
        answer = min(answer, getMinValue());
        return;
    }
    // 현재 배열 정보 저장해놓음
    copy(A, B);
    for (int i = 0; i < K; i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            dfs(i, cnt + 1);
            visited[i] = false;
            // 이전에 저장해놓은 배열 정보 다시 받아옴
            copy(B, A);
        }
    }
}

int main()
{
    int r, c, s;
    cin >> N >> M >> K;
    visited.assign(K, false);

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= M; j++)
        {
            cin >> A[i][j];
        }
    }

    for (int i = 0; i < K; i++)
    {
        cin >> r >> c >> s;
        operation.push_back({r, c, s});
    }

    dfs(0, 0);
    cout << answer;

    return 0;
}