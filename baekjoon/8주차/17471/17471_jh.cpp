#include <iostream>
#include <vector>
#include <string.h>
#include <queue>
#include <algorithm>
using namespace std;
#define nMAX 11
// 바보같이 인구수 차이 최대값을 100으로 설정해놔갖고 장장 두시간을 헤맸다...나는 바보
#define differenceMAX 1000
// 구역별 인구수 저장
int people[nMAX];
int N, difference = differenceMAX;
// A선거구와 B선거구 정보
vector<int> aArea, bArea;
// 방문정보와 구역간 연결정보 저장
bool visited[nMAX], area[nMAX][nMAX];
// 선거구내 구역간의 연결여부에 따라 구내 인구수 합이나 -1을 반환
int bfs(int start, int size, bool isAArea)
{
    queue<int> needVisit;
    int areaCnt = 1, peopleTotal = people[start];
    bool tempVisited[nMAX] = {false};
    tempVisited[start] = true;
    needVisit.push(start);
    while (!needVisit.empty())
    {
        int current = needVisit.front();
        needVisit.pop();
        for (int i = 1; i <= N; i++)
        {
            // 1. 현재 구역과 탐색하려는 구역이 연결되어 있고
            // 2. 탐색 구역이 해당 선거구내에 포함되어 있고
            // 3. 탐색 구역을 아직 방문하지 않았다면
            if (area[current][i] && visited[i] == isAArea && !tempVisited[i])
            {
                tempVisited[i] = true;
                areaCnt++;
                peopleTotal += people[i];
                needVisit.push(i);
            }
        }
    }
    // 해당 선거구내 구역들이 모두 연결되어 있을 경우
    if (areaCnt == size)
    {
        return peopleTotal;
    }
    else
    {
        return -1;
    }
}
// 선거구를 나누는 함수
bool setArea()
{
    for (int i = 1; i <= N; i++)
    {
        // 해당 구역이 A선거구라면
        if (visited[i])
        {
            aArea.push_back(i);
        }
        // 해당 구역이 B선거구라면
        else
        {
            bArea.push_back(i);
        }
    }
    // B선거구에 구역이 한개도 포함되어 있지 않다면
    if (bArea.size() == 0)
    {
        return false;
    }
    else
    {
        return true;
    }
}
// 조합을 통해 A선거구에 포함되는 구역 정보 구함
void dfs(int current, int cnt)
{
    // A선거구에 구역이 하나라도 존재한다면
    // (A선거구에 포함될 수 있는 구역 수가 정해져있지않기 때문에 모든 경우를 검사)
    if (cnt >= 1)
    {
        aArea.clear();
        bArea.clear();
        if (setArea())
        {
            // A선거구 내 인구수와 B선거구 내 인구수 구함
            int aAreaPeople = bfs(aArea[0], aArea.size(), true), bAreaPeople = bfs(bArea[0], bArea.size(), false);
            // A선거구와 B선거구 내 구역들이 모두 연결되어 있다면
            if (aAreaPeople != -1 && bAreaPeople != -1)
            {
                // 두 선거구 인구수 차이 최소값을 구함
                difference = min(difference, abs(aAreaPeople - bAreaPeople));
            }
        }
    }
    for (int i = current; i <= N; i++)
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
    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        cin >> people[i];
    }

    for (int i = 1; i <= N; i++)
    {
        int cnt, num;
        cin >> cnt;
        for (int j = 0; j < cnt; j++)
        {
            cin >> num;
            area[i][num] = true;
        }
    }
    // 조합 구현
    dfs(1, 0);

    if (difference == differenceMAX)
    {
        difference = -1;
    }

    cout << difference;

    return 0;
}