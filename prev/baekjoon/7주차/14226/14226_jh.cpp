#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
#define MAX 1001

int S;
bool visited[MAX][MAX];

int bfs()
{
    queue<vector<int>> needVisit;
    // 화면 상태, 클립보드 상태, 계산 시간 저장
    needVisit.push({1, 0, 0});
    visited[1][0] = true;

    while (!needVisit.empty())
    {
        int screen = needVisit.front()[0];
        int clipboard = needVisit.front()[1];
        int time = needVisit.front()[2];
        needVisit.pop();
        // 이모티콘 다 만들어지면
        if (screen == S)
        {
            return time;
        }
        // 화면의 임티 개수가 연산 가능한 경우라면
        if (screen > 0 && screen < MAX)
        {
            if (!visited[screen][screen])
            {
                needVisit.push({screen, screen, time + 1});
                visited[screen][screen] = true;
            }
            if (clipboard > 0 && screen + clipboard < MAX)
            {
                if (!visited[screen + clipboard][clipboard])
                {
                    needVisit.push({screen + clipboard, clipboard, time + 1});
                    visited[screen + clipboard][clipboard] = true;
                }
            }
            if (!visited[screen - 1][clipboard])
            {
                needVisit.push({screen - 1, clipboard, time + 1});
                visited[screen - 1][clipboard] = true;
            }
        }
    }
}

int main()
{
    cin >> S;
    cout << bfs();

    return 0;
}