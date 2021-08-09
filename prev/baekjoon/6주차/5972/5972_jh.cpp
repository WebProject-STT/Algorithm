#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define INF 1e9
#define MAX 50001

int N;
int dist[MAX];
vector<pair<int, int>> MAP[MAX];

int Dijkstra(int start)
{
    priority_queue<pair<int, int>> pq;
    dist[start] = 0;
    pq.push({-dist[start], start});

    while (!pq.empty())
    {
        int currentDistance = -pq.top().first;
        int current = pq.top().second;
        int size = MAP[current].size();
        pq.pop();
        if (currentDistance > dist[current])
        {
            continue;
        }
        for (int i = 0; i < size; i++)
        {
            int next = MAP[current][i].first;
            int nextDistance = MAP[current][i].second + currentDistance;
            if (nextDistance < dist[next])
            {
                dist[next] = nextDistance;
                pq.push({-dist[next], next});
            }
        }
    }
    return dist[N];
}

int main(void)
{
    int M, a, b, c;
    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b >> c;
        MAP[a].push_back({b, c});
        MAP[b].push_back({a, c});
    }
    fill(dist, dist + MAX, INF);
    cout << Dijkstra(1);
}