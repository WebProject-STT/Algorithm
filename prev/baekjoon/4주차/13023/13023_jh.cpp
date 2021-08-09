#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MAX 2000
// 친구 관계를 저장할 벡터
vector<vector<int>> relation;
// 방문 표시할 벡터
vector<bool> visited;

int bfs(int current, int cnt)
{
    // 반복문 진행 시 size 계속 계산하지 않도록 미리 변수로 선언해놓음
    int size = relation[current].size();
    // 조건 만족할 경우 true 반환
    if (cnt == 4)
    {
        return true;
    }

    for (int i = 0; i < size; i++)
    {
        int next = relation[current][i];
        if (!visited[next])
        {
            visited[next] = true;
            // 조건 만족할 경우 여기서도 true 반환
            if (bfs(next, cnt + 1))
            {
                return true;
            }
            visited[next] = false;
        }
    }

    return false;
}

int main()
{
    int N, M, answer = 0;

    cin >> N >> M;
    relation.resize(N);
    visited.assign(N, false);

    for (int i = 0; i < M; i++)
    {
        int a, b;
        cin >> a >> b;
        // 친구 관계 입력받고 상호연결
        relation[a].push_back(b);
        relation[b].push_back(a);
    }

    for (int i = 0; i < N; i++)
    {
        // 현재 지점은 방문표시
        visited[i] = true;
        // 조건에 맞는 친구 관계가 존재할 경우 반복문 종료
        if (bfs(i, 0))
        {
            answer = 1;
            break;
        }
        // 방문 벡터 초기화
        visited.assign(N, false);
    }

    cout << answer;

    return 0;
}