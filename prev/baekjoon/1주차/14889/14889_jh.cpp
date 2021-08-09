#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
#define MAX 20

int stats[MAX][MAX];
int people, peopleHalf, answer = 40000;
// 능력치의 합을 반환하는 함수
int getTotalStats(vector<int> team)
{
    int totalStats = 0;
    for (int i = 0; i < peopleHalf; i++)
    {
        for (int j = 0; j < peopleHalf; j++)
        {
            totalStats += stats[team[i]][team[j]];
        }
    }
    return totalStats;
}

int main()
{
    // 조합에 쓰일 임시배열
    vector<int> temp;

    cin >> people;
    peopleHalf = people / 2;

    for (int i = 0; i < people; i++)
    {
        for (int j = 0; j < people; j++)
        {
            cin >> stats[i][j];
        }
    }

    for (int i = 0; i < peopleHalf; i++)
    {
        temp.push_back(0);
        temp.push_back(1);
    }
    // next_permutation 사용하기 위해서는 배열 정렬해야함
    sort(temp.begin(), temp.end());

    do
    {
        vector<int> start, link;
        int statsDifference;
        for (int i = 0; i < people; i++)
        {
            // 스타트팀과 링크팀으로 나눔
            temp[i] == 1 ? start.push_back(i) : link.push_back(i);
        }
        statsDifference = abs(getTotalStats(start) - getTotalStats(link));
        answer = min(answer, statsDifference);
    } while (next_permutation(temp.begin(), temp.end()));

    cout << answer;
}