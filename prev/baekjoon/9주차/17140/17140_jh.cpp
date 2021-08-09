#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define MAX 101
// 항상 범위를 신경쓰자..!^^
// 수의 등장 횟수와 크기를 이용해 정렬하는 함수
bool cmp(pair<int, int> a, pair<int, int> b)
{
    if (a.second < b.second)
    {
        return true;
    }
    else if (a.second == b.second)
    {
        return a.first <= b.first;
    }
    else
    {
        return false;
    }
}

int main()
{
    int r, c, k, time = 0;
    int h = 3, y = 3;
    int MAP[MAX][MAX];

    cin >> r >> c >> k;

    for (int i = 1; i <= h; i++)
    {
        for (int j = 1; j <= y; j++)
        {
            cin >> MAP[i][j];
        }
    }

    while (1)
    {
        if (MAP[r][c] == k)
        {
            break;
        }
        if (time > 100)
        {
            time = -1;
            break;
        }
        if (h >= y)
        {
            // 각 행의 수 등장 횟수와 수의 크기 저장하는 벡터
            vector<vector<int>> changeMAP;
            changeMAP.resize(h + 1);
            for (int i = 1; i <= h; i++)
            {
                int cnt[MAX] = {0};
                for (int j = 1; j <= y; j++)
                {
                    // 수 등장 횟수 계산
                    cnt[MAP[i][j]]++;
                }
                // 수 등장 횟수와 수의 크기 쌍으로 저장하는 벡터
                vector<pair<int, int>> numCnt;
                for (int k = 1; k < MAX; k++)
                {
                    // k가 한번이라도 등장했다면
                    if (cnt[k] > 0)
                    {
                        // numCnt에 저장
                        numCnt.push_back({k, cnt[k]});
                    }
                }
                // 주어진 조건대로 정렬
                sort(numCnt.begin(), numCnt.end(), cmp);
                for (auto elem : numCnt)
                {
                    // 수의 등장횟수, 크기 저장
                    changeMAP[i].push_back(elem.first);
                    changeMAP[i].push_back(elem.second);
                }
            }
            int maxY = 0;
            // 가장 큰 열의 크기를 구함
            for (int i = 1; i <= h; i++)
            {
                int size = changeMAP[i].size();
                maxY = max(maxY, size);
            }
            if (maxY > 100)
            {
                maxY = 100;
            }
            // MAP배열 확장
            for (int i = 1; i <= h; i++)
            {
                int start = changeMAP[i].size();
                for (int j = 1; j <= start; j++)
                {
                    MAP[i][j] = changeMAP[i][j - 1];
                }
                for (int j = start + 1; j <= maxY; j++)
                {
                    MAP[i][j] = 0;
                }
            }
            y = maxY;
        }
        else
        {
            vector<vector<int>> changeMAP;
            changeMAP.resize(y + 1);
            for (int j = 1; j <= y; j++)
            {
                int cnt[MAX] = {0};
                for (int i = 1; i <= h; i++)
                {
                    cnt[MAP[i][j]]++;
                }
                vector<pair<int, int>> numCnt;

                for (int k = 1; k < MAX; k++)
                {
                    if (cnt[k] > 0)
                    {
                        numCnt.push_back({k, cnt[k]});
                    }
                }

                sort(numCnt.begin(), numCnt.end(), cmp);
                for (auto elem : numCnt)
                {
                    changeMAP[j].push_back(elem.first);
                    changeMAP[j].push_back(elem.second);
                }
            }
            int maxH = 0;
            for (int j = 1; j <= y; j++)
            {
                int size = changeMAP[j].size();
                maxH = max(maxH, size);
            }
            if (maxH > 100)
            {
                maxH = 100;
            }
            for (int j = 1; j <= y; j++)
            {
                int start = changeMAP[j].size();
                for (int i = 1; i <= start; i++)
                {
                    MAP[i][j] = changeMAP[j][i - 1];
                }
                for (int i = start + 1; i <= maxH; i++)
                {
                    MAP[i][j] = 0;
                }
            }
            h = maxH;
        }
        time++;
    }

    cout << time;

    return 0;
}