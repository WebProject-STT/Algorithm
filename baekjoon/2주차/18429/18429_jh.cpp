#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, K, answer = 0;
vector<int> kit;
vector<bool> visited;
// 처음에는 next_permutation으로 구현했으나 오답 떠서 dfs로 구현함
// dfs로 순열 구현 (중량 합과 운동 횟수가 매개변수)
void dfs(int total, int cnt)
{
    // 중량 합이 500보다 작으면 리턴
    if (total < 500)
    {
        return;
    }
    // 운동 횟수 다 채우면 리턴
    if (N == cnt)
    {
        answer++;
        return;
    }
    for (int i = 0; i < N; i++)
    {
        if (!visited[i])
        {
            // 방문표시
            visited[i] = true;
            dfs(total + kit[i], cnt + 1);
            // 해당 정점은 이후에 재방문해야 되므로 방문 표시 없앰
            visited[i] = false;
        }
    }
}

int main()
{
    int addWeight;

    cin >> N >> K;
    visited.assign(N, false);

    for (int i = 0; i < N; i++)
    {
        cin >> addWeight;
        // 중량 최종 증가량을 저장
        kit.push_back(addWeight - K);
    }

    dfs(500, 0);

    cout << answer;

    return 0;
}