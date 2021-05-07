#include <algorithm>
#include <iostream>
using namespace std;
#define MAX 201
/*
    union-find 사용
    각 도시의 루트노드가 모두 같다면 연결 되어 있다는 뜻!
    => 동혁이는 여행을 갈 수 있음
    ** 플로이드 와샬로 푼 사람도 있었음
*/
// 각 도시의 부모 도시를 저장
int parent[MAX];
// 부모 도시 찾음
int getParent(int x)
{
    if (parent[x] != x)
    {
        parent[x] = getParent(parent[x]);
    }
    return parent[x];
}
// 다른 두 도시의 부모 노드를 합침 => 도시 연결
void unionParent(int a, int b)
{
    int parentA = getParent(a);
    int parentB = getParent(b);
    if (parentA < parentB)
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

    int N, M, link;
    int *travel;
    bool check = true;

    cin >> N >> M;
    travel = new int[M];

    for (int i = 1; i <= N; i++)
    {
        parent[i] = i;
    }

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> link;
            // i와 j가 연결되어 있다면 부모도 합쳐줌
            if (link == 1)
            {
                unionParent(i, j);
            }
        }
    }

    for (int i = 0; i < M; i++)
    {
        cin >> travel[i];
    }

    for (int i = 0; i < M - 1; i++)
    {
        // 여행가려는 도시들의 부모노드가 하나라도 같지 않다면
        // check는 false로 변경
        if (getParent(travel[i]) != getParent(travel[i + 1]))
        {
            check = false;
            break;
        }
    }
    // 여행 계획 도시들이 모두 연결되어 있다면 yes 출력
    if (check)
    {
        cout << "YES";
    }
    // 아니면 no 출력
    else
    {
        cout << "NO";
    }

    return 0;
}