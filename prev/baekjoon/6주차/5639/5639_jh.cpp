#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 10000

int node[MAX];
// 후위 순회 결과 출력하는 함수
void postOrder(int root, int start, int end)
{
    int rightIndex = end + 1;
    // 현재 방문노드가 리프노드라면 노드 출력 후 반환
    if (start > end)
    {
        cout << root << '\n';
        return;
    }
    // 오른쪽 서브 트리의 시작 지점을 찾음
    for (int i = start; i <= end; i++)
    {
        if (root < node[i])
        {
            rightIndex = i;
            break;
        }
    }
    // 왼쪽 서브트리 방문
    // (왼쪽 서브트리가 존재하는 경우에만 방문할 수 있도록 조건문 넣음)
    if (start != rightIndex)
    {
        postOrder(node[start], start + 1, rightIndex - 1);
    }
    // 오른쪽 서브트리 방문
    // (오른쪽 서브트리가 존재하는 경우에만 방문할 수 있도록 조건문 넣음)
    if (rightIndex != end + 1)
    {
        postOrder(node[rightIndex], rightIndex + 1, end);
    }
    // 리프 노드들을 다 방문했다면 루트 노드 출력
    cout << root << '\n';
}

int main()
{
    int num, index = 0;
    // 노드 정보 입력 받음
    while (cin >> num)
    {
        node[index++] = num;
    }
    // 함수 호출
    postOrder(node[0], 1, index - 1);

    return 0;
}