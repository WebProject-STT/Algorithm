#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
#define MAX 6

char MAP[MAX][MAX];
// 선생님 위치 저장
vector<pair<int, int>> teacher;
int N;
// 선생님과 마주치는 학생이 있는지 확인
bool check()
{
    bool result = true;
    for (auto elem : teacher)
    {
        int currentX = elem.first;
        int currentY = elem.second;
        // 상
        for (int i = currentX - 1; i >= 0; i--)
        {
            if (MAP[i][currentY] == 'O')
                break;
            if (MAP[i][currentY] == 'S')
                return false;
        }
        // 하
        for (int i = currentX + 1; i < N; i++)
        {
            if (MAP[i][currentY] == 'O')
                break;
            if (MAP[i][currentY] == 'S')
                return false;
        }
        // 좌
        for (int i = currentY - 1; i >= 0; i--)
        {
            if (MAP[currentX][i] == 'O')
                break;
            if (MAP[currentX][i] == 'S')
                return false;
        }
        // 우
        for (int i = currentY + 1; i < N; i++)
        {
            if (MAP[currentX][i] == 'O')
                break;
            if (MAP[currentX][i] == 'S')
                return false;
        }
    }
    return result;
}

bool dfs(int cnt)
{
    // 벽을 3개 세우면 check함수 호출 결과 반환
    if (cnt == 3)
    {
        return check();
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // 빈 공간이면
            if (MAP[i][j] == 'X')
            {
                //벽 세움
                MAP[i][j] = 'O';
                if (dfs(cnt + 1))
                {
                    return true;
                }
                MAP[i][j] = 'X';
            }
        }
    }
    return false;
}

int main()
{
    string answer = "NO";
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> MAP[i][j];
            if (MAP[i][j] == 'T')
            {
                teacher.push_back({i, j});
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (MAP[i][j] == 'X')
            {
                MAP[i][j] = 'O';
                if (dfs(1))
                {
                    answer = "YES";
                    goto EXIT;
                }
                MAP[i][j] = 'X';
            }
        }
    }

EXIT:
    cout << answer;

    return 0;
}