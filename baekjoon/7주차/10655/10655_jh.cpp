#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    // 체크포인트간 거리를 저장 (distance[1] => 0번째 체크포인트와 1번째 체크포인트 간 거리)
    vector<int> distance;
    // 체크포인트의 좌표 저장
    vector<pair<int, int>> point;
    int N, x, y, answer = 0;
    // 모든 체크포인트를 들렀을 때의 거리, 체크포인트를 건너뛰었을 때 감소되는 거리의 최대값
    int total = 0, skip = 0;

    cin >> N;
    distance.resize(N);

    for (int i = 0; i < N; i++)
    {
        cin >> x >> y;
        point.push_back({x, y});
    }

    for (int i = 1; i < N; i++)
    {
        distance[i] = abs(point[i].first - point[i - 1].first) + abs(point[i].second - point[i - 1].second);
        total += distance[i];
    }

    for (int i = 1; i < N - 1; i++)
    {
        // i번째를 건너뛸 경우
        // i - 1 <-> i, i <-> i + 1는 빼야됨
        int remove = distance[i] + distance[i + 1];
        // i <-> i + 1는 더해야됨
        int add = abs(point[i + 1].first - point[i - 1].first) + abs(point[i + 1].second - point[i - 1].second);
        // 결국 remove - add가 최대값일 때 최소 거리를 구할 수 있음
        skip = max(skip, remove - add);
    }

    cout << total - skip;

    return 0;
}