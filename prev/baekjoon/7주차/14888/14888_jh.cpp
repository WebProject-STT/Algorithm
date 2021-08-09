#include <iostream>
#include <algorithm>
using namespace std;
#define sizeMAX 11
#define numMAX 1000000000
// 시간 0ms 걸림
// 입력받은 수와 연산자의 갯수 저장하는 배열
int arr[sizeMAX], operatorNum[4];
int N, maxNum = -numMAX, minNum = numMAX;
// 매개변수는 현재 식의 결과값과 총 연산자 사용 횟수
void dfs(int curNum, int cnt)
{
    // 연산자를 모두 사용하면 최대값과 최소값 갱신 후 리턴
    if (cnt == N - 1)
    {
        maxNum = max(curNum, maxNum);
        minNum = min(curNum, minNum);
        return;
    }
    for (int i = 0; i < 4; i++)
    {
        int nextNum;
        // 해당 연산자의 연산 횟수가 남아있을 경우
        // (visited 배열 사용하던 방식과 동일하다고 보면 됨)
        if (operatorNum[i] > 0)
        {
            operatorNum[i]--;
            if (i == 0)
            {
                nextNum = curNum + arr[cnt + 1];
            }
            else if (i == 1)
            {
                nextNum = curNum - arr[cnt + 1];
            }
            else if (i == 2)
            {
                nextNum = curNum * arr[cnt + 1];
            }
            else
            {
                nextNum = curNum / arr[cnt + 1];
            }
            dfs(nextNum, cnt + 1);
            operatorNum[i]++;
        }
    }
}

int main()
{
    int idxNum = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < 4; i++)
    {
        cin >> operatorNum[i];
    }
    // 숫자의 순서는 바뀌지 않으므로 연산 과정의 첫번째 값은 arr의 첫번째 원소
    dfs(arr[0], 0);

    cout << maxNum << '\n';
    cout << minNum << '\n';

    return 0;
}

/* visited 배열을 이용하는 방법, 이것도 정답인데 156ms 시간이 소요되서 다른 방법 찾음 
int arr[sizeMAX], operatorNum[sizeMAX - 1];
bool visited[sizeMAX - 1] = {false};
int N, maxNum = -numMAX, minNum = numMAX;

void dfs(int curNum, int cnt)
{
    if (cnt == N - 1)
    {
        maxNum = max(curNum, maxNum);
        minNum = min(curNum, minNum);
        return;
    }
    for (int i = 0; i < N - 1; i++)
    {
        int nextNum;
        int curOperator = operatorNum[i];
        if (!visited[i])
        {
            visited[i] = true;
            if (curOperator == 0)
            {
                nextNum = curNum + arr[cnt + 1];
            }
            else if (curOperator == 1)
            {
                nextNum = curNum - arr[cnt + 1];
            }
            else if (curOperator == 2)
            {
                nextNum = curNum * arr[cnt + 1];
            }
            else
            {
                nextNum = curNum / arr[cnt + 1];
            }
            dfs(nextNum, cnt + 1);
            visited[i] = false;
        }
    }
}

int main()
{
    int idxNum = 0;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < 4; i++)
    {
        int num, tempNum = idxNum;
        cin >> num;
        for (int j = tempNum; j < tempNum + num; j++)
        {
            operatorNum[j] = i;
            idxNum++;
        }
    }

    dfs(arr[0], 0);

    cout << maxNum << '\n';
    cout << minNum << '\n';

    return 0;
}
*/