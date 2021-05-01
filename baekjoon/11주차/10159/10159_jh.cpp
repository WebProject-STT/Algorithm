#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
/*
    물건들간의 연결관계를 확인하는 문제
    플로이드 와샬 알고리즘 적용 => '거쳐가는 정점'을 기준으로 최단 거리를 구하는 알고리즘
    여기서는 최단 거리가 아닌 연결 여부를 구한다
    예) A > B, B > C => B > C
        => 여기서 거쳐가는 정점은 B이고 B를 통해 A와 C가 연결되는지를 확인
*/
int N;
// 물건 간 연결 여부를 저장하는 벡터
vector<vector<bool>> link;

void floyd()
{
    // k는 거쳐가는 정점
    for (int k = 1; k <= N; k++)
    {
        // i는 출발점
        for (int i = 1; i <= N; i++)
        {
            // 출발점과 거쳐가는 정점이 같으면 확인할 필요가 없으므로 continue
            if (i == k)
            {
                continue;
            }
            //j는 도착점
            for (int j = 1; j <= N; j++)
            {
                // i-k 연결, k-j 연결 되어 있다면
                if (link[i][k] && link[k][j])
                {
                    // i-j도 연결됨
                    link[i][j] = true;
                }
            }
        }
    }
}

int main()
{
    int M, x, y;

    cin >> N;
    cin >> M;
    link.assign(N + 1, vector<bool>(N + 1, false));
    // 자기자신은 연결되어 있음
    for (int i = 1; i <= N; i++)
    {
        link[i][i] = true;
    }

    for (int i = 0; i < M; i++)
    {
        cin >> x >> y;
        link[x][y] = true;
    }

    floyd();

    for (int i = 1; i <= N; i++)
    {
        int cnt = 0;
        for (int j = 1; j <= N; j++)
        {
            // i-j 연결 안되있고 j-i도 연결 안되있다면 i와 j간 비교 결과 알 수 없음
            if (!link[i][j] && !link[j][i])
            {
                cnt++;
            }
        }
        cout << cnt << '\n';
    }

    return 0;
}