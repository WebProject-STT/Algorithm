#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
#define MAX 100001
#define INF 1e9

int K;
// 다익스트라 구현
int dijkstra(int start)
{
    priority_queue<pair<int, int>> needVisit;
    int minTime[MAX];
    needVisit.push({0, start});
    fill(minTime, minTime + MAX, INF);
    minTime[start] = 0;

    while (!needVisit.empty())
    {
        int time = -needVisit.top().first;
        int current = needVisit.top().second;
        // 현재 지점에서 갈 수 있는 곳들 저장
        int next[3] = {current - 1, current + 1, current * 2};
        needVisit.pop();
        if (time > minTime[current])
        {
            continue;
        }
        for (int i = 0; i < 3; i++)
        {
            // 순간이동 할 때는 시간이 증가되지 않기 때문에 다음과 같이 변수 선언
            int nextTime = i == 2 ? time : time + 1;
            if (next[i] < 0 || next[i] >= MAX || nextTime >= minTime[next[i]])
            {
                continue;
            }
            minTime[next[i]] = nextTime;
            needVisit.push({-nextTime, next[i]});
        }
    }
    return minTime[K];
}

int main(void)
{
    int N;
    cin >> N >> K;

    cout << dijkstra(N);
    return 0;
}