#include <vector>
#include <queue>
#include <iostream>
using namespace std;
// 컴퓨터 개수와 연결 개수
int computer, computer_pair;
// 네트워크 상태
vector<vector<int>> network;

int bfs()
{
    // 시작노드는 1
    // 아래 반복문에서 시작노드를 검사할때도 바이러스 개수를 1 증가시키므로 -1로 설정
    int start = 1, virus = -1;
    // 다음에 방문할 지점 저장
    queue<int> need_visit;
    // 방문 지점 저장
    vector<bool> visited(computer + 1, 0);
    need_visit.push(start);
    // 시작점 방문 표시
    visited[start] = true;

    while (!need_visit.empty())
    {
        int current = need_visit.front();
        need_visit.pop();
        // 바이러스 1 증가
        virus++;
        // 현재 지점과 연결된 지점들 검사
        for (int i = 0; i < network[current].size(); i++)
        {
            // 현재 지점과 연결된 지점
            int next = network[current][i];
            // 해당 지점을 아직 방문하지 않았다면
            if (!visited[next])
            {
                // 방문 표시
                visited[next] = true;
                // 다음에 방문할 지점으로 넣음
                need_visit.push(next);
            }
        }
    }
    return virus;
}

int main()
{
    cin >> computer;
    cin >> computer_pair;
    network.resize(computer + 1);
    int a, b;

    for (int i = 0; i < computer_pair; i++)
    {
        cin >> a >> b;
        // 네트워크 연결
        network[a].push_back(b);
        network[b].push_back(a);
    }

    cout << bfs();
}