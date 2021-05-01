#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define MAX 51

int parent[MAX];
vector<int> knowingPeople;
vector<vector<int>> party;
/*
    union-find 알고리즘 사용
    같은 파티에 참여한적 있는 사람들은 모두 같은 부모노드를 가진다.(같은 집합에 속하게 된다)
    각 파티에 참석한 인원을 검사
    => 진실을 알고 있는 사람과 같은 파티를 참가한 적이 있는 사람이 있다면 해당 파티에서
       지민이는 진실만을 말해야 한다.
*/
// 부모노드(루트노드) 확인
int getParent(int x)
{
    if (parent[x] != x)
    {
        parent[x] = getParent(parent[x]);
    }
    return parent[x];
}
// 부모노드를 합침
// => a노드와 b노드를 같은 집합에 속하게 한다
void unionParent(int a, int b)
{
    int parentA = getParent(a);
    int parentB = getParent(b);
    if (parentA <= parentB)
    {
        parent[parentB] = parentA;
    }
    else
    {
        parent[parentA] = parentB;
    }
}

int main()
{
    int N, M, answer = 0;
    int truthCnt, truthNum, peopleCnt, peopleNum;

    cin >> N >> M;
    cin >> truthCnt;
    party.resize(M);
    // 처음 각 노드의 부모노드는 자기 자신
    for (int i = 1; i <= N; i++)
    {
        parent[i] = i;
    }
    // 진실을 알고 있는 사람 입력받음
    for (int i = 0; i < truthCnt; i++)
    {
        cin >> truthNum;
        knowingPeople.push_back(truthNum);
    }

    for (int i = 0; i < M; i++)
    {
        int previous = 0;
        cin >> peopleCnt;
        for (int j = 0; j < peopleCnt; j++)
        {
            cin >> peopleNum;
            if (previous != 0)
            {
                // 같은 파티에 참가한 사람들 모두 연결
                unionParent(previous, peopleNum);
            }
            previous = peopleNum;
            party[i].push_back(peopleNum);
        }
    }

    for (int i = 0; i < M; i++)
    {
        bool isTruth = false;
        for (auto elem : party[i])
        {
            // 해당 파티에 참가한 사람 중 진실을 아는 사람과 같은 파티에 참가한 사람이 있는지 확인
            for (auto knowingNum : knowingPeople)
            {
                if (getParent(elem) == getParent(knowingNum))
                {
                    isTruth = true;
                    break;
                }
            }
            if (isTruth)
            {
                break;
            }
        }
        if (!isTruth)
        {
            answer++;
        }
    }

    cout << answer;

    return 0;
}