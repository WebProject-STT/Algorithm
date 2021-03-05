#include <iostream>
#include <queue>
using namespace std;
#define MAX 100001

int A, B, N, M;
int visited[MAX] = {0};

int bfs()
{
    // 방문할 지점과 이동횟수 저장
    queue<pair<int, int>> need_visit;
    need_visit.push({N, 0});
    visited[N] = true;

    while (!need_visit.empty())
    {
        int current = need_visit.front().first;
        int cnt = need_visit.front().second;
        need_visit.pop();
        // 주미를 만나면 이동횟수 반환
        if (current == M)
        {
            return cnt;
        }
        // 현재 위치에서 동규가 갈 수 있는 지점들
        int next[8] = {current + 1, current - 1, current + A, current - A, current + B, current - B, current * A, current * B};

        for (int i = 0; i < 8; i++)
        {
            // 이동하려는 지점이 칸 범위를 벗어나거나 이미 방문했다면 continue
            if ((next[i] < 0 || next[i] > MAX - 1) || visited[next[i]])
            {
                continue;
            }
            visited[next[i]] = true;
            need_visit.push({next[i], cnt + 1});
        }
    }
}

int main()
{
    cin >> A >> B >> N >> M;

    cout << bfs();

    return 0;
}