#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define INF 1e9
#define MAX 50

int city[MAX][MAX], N, M, answer = INF;
// 집과 치킨집 개수 저장
int houseCnt, chickenCnt;
// 집과 치킨집 위치 저장
vector<pair<int, int>> house, chicken;
// 조합 구현 위한 방문 표시 벡터
vector<bool> visited;
// 치킨 거리 최소합 구하는 함수
int getMinDistance()
{
    int totalDistance = 0;
    for (int i = 0; i < houseCnt; i++)
    {
        int minDistance = INF;
        int houseX = house[i].first, houseY = house[i].second;
        for (int j = 0; j < chickenCnt; j++)
        {
            // 방문한 치킨집이라면 (치킨집이 조합 원소?에 들어간다면)
            if (visited[j])
            {
                int distance = abs(houseX - chicken[j].first) + abs(houseY - chicken[j].second);
                // 현재 집과 가장 가까운 치킨집 거리 구함
                if (minDistance > distance)
                {
                    minDistance = distance;
                }
            }
        }
        totalDistance += minDistance;
    }
    return totalDistance;
}
// 조합
void dfs(int current, int cnt)
{
    if (cnt == M)
    {
        answer = min(answer, getMinDistance());
    }
    for (int i = current; i < chickenCnt; i++)
    {
        if (!visited[i])
        {
            visited[i] = true;
            dfs(i, cnt + 1);
            visited[i] = false;
        }
    }
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> city[i][j];
            if (city[i][j] == 1)
            {
                house.push_back({i, j});
            }
            else if (city[i][j] == 2)
            {
                chicken.push_back({i, j});
            }
        }
    }
    houseCnt = house.size();
    chickenCnt = chicken.size();
    visited.assign(chickenCnt, false);

    dfs(0, 0);

    cout << answer;

    return 0;
}