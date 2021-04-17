#include <algorithm>
#include <iostream>
using namespace std;
#define MAX 100

int N, L, answer = 0;
// 경사로 건설 여부 표시하는 배열
bool road[MAX][MAX];
// 경사로 배열 초기화
void init()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            road[i][j] = false;
        }
    }
}
// 길 건널 수 있는지 확인
void roadCheck(int MAP[][MAX])
{
    int cnt = 0;
    init();

    for (int j = 0; j < N; j++)
    {
        bool check = true;
        int previous = MAP[0][j];
        for (int i = 1; i < N; i++)
        {
            int current = MAP[i][j];
            // 현재칸과 이전칸의 크기가 2이상 차이난다면 길을 건널 수 없음
            if (abs(current - previous) >= 2)
            {
                check = false;
                break;
            }
            // 내리막길 만듬
            else if (previous - current == 1)
            {
                for (int k = i; k < i + L; k++)
                {
                    // 해당 칸에 아직 경사로가 건설되지 않았고 길을 만들 수 있다면
                    if (k < N && !road[k][j] && current == MAP[k][j])
                    {
                        // 경사로 건설
                        road[k][j] = true;
                    }
                    else
                    {
                        check = false;
                        break;
                    }
                }
                i += L - 1;
            }
            // 오르막길 만듬
            else if (current - previous == 1)
            {
                for (int k = i - 1; k >= i - L; k--)
                {
                    // 해당 칸에 아직 경사로가 건설되지 않았고 길을 만들 수 있다면
                    if (k >= 0 && !road[k][j] && previous == MAP[k][j])
                    {
                        // 경사로 건설
                        road[k][j] = true;
                    }
                    else
                    {
                        check = false;
                        break;
                    }
                }
            }
            previous = current;
        }
        // 길을 건널 수 있다면
        if (check)
        {
            // 건널 수 있는 길의 개수 1 증가
            answer++;
        }
    }
}

int main()
{

    cin >> N >> L;
    // 입력 배열, 행과 열이 뒤바뀐 배열
    int MAP[MAX][MAX], MAP2[MAX][MAX];

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> MAP[i][j];
            MAP2[j][i] = MAP[i][j];
        }
    }

    roadCheck(MAP);
    roadCheck(MAP2);

    cout << answer;

    return 0;
}