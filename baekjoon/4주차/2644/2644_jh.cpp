#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int firstNum, secondNum;
vector<vector<int>> relation;
vector<bool> visited;

int dfs(int current, int cnt)
{
    int size = relation[current].size();
    // current가 원하는 사람일 경우 cnt를 반환
    if (current == secondNum)
    {
        return cnt;
    }

    for (int i = 0; i < size; i++)
    {
        int next = relation[current][i];
        if (!visited[next])
        {
            visited[next] = true;
            int result = dfs(next, cnt + 1);
            // 촌수 관계를 계산한 경우 결과값 반환
            if (result != -1)
            {
                return result;
            }
        }
    }

    return -1;
}

int main()
{
    int N, M;
    cin >> N;
    cin >> firstNum >> secondNum;
    cin >> M;
    relation.resize(N + 1);
    visited.assign(N + 1, false);

    for (int i = 0; i < M; i++)
    {
        int x, y;
        cin >> x >> y;
        // 관계 연결
        relation[x].push_back(y);
        relation[y].push_back(x);
    }

    visited[firstNum] = true;
    cout << dfs(firstNum, 0);

    return 0;
}