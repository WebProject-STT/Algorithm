#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define MAX 50

int N, M;
bool arrA[MAX][MAX], arrB[MAX][MAX];
// A의 부분 배열과 B의 부분 배열이 일치하는지 확인
// (배열이 뒤집기 연산을 수행할 수 없다면 전체 배열을 비교함)
int checkSame(int startX, int startY, int cnt)
{
    // 두 배열 일치하는지 확인
    for (int i = startX; i < N; i++)
    {
        for (int j = startY; j < M; j++)
        {
            if (arrA[i][j] != arrB[i][j])
            {
                return -1;
            }
        }
    }
    return cnt;
}
// 뒤집기 연산 수행
void reverse(int currentX, int currentY)
{
    int endX = currentX + 3, endY = currentY + 3;
    for (int i = currentX; i < endX; i++)
    {
        for (int j = currentY; j < endY; j++)
        {
            arrA[i][j] = !arrA[i][j];
        }
    }
}
// A 부분배열과 B 부분배열에서 특정 위치 원소들의 일치 갯수 반환
/*
    맨 오른쪽 부분배열을 확인하는 경우
    - 해당 부분배열의 첫번째 행을 검사
    맨 아래쪽 부분배열을 확인하는 경우
    - 해당 부분배열의 첫번째 열을 검사
*/
int getSameCnt(int currentX, int currentY, bool isBottom)
{
    int cnt = 0;
    bool same;
    int start = isBottom ? currentX : currentY;
    int end = start + 3;
    for (int i = start; i < end; i++)
    {
        if (isBottom)
        {
            same = arrA[i][currentY] == arrB[i][currentY];
        }
        else
        {
            same = arrA[currentX][i] == arrB[currentX][i];
        }
        cnt = same ? cnt + 1 : cnt;
    }
    return cnt;
}
// 뒤집기 연산을 수행한 횟수를 반환
int getReverseCnt()
{
    int cnt = 0, sameCnt;
    for (int i = 0; i < N - 2; i++)
    {
        for (int j = 0; j < M - 2; j++)
        {
            // 맨 오른쪽이나 아래쪽 부분배열을 확인하는 경우
            if (i == N - 3 || j == M - 3)
            {
                sameCnt = getSameCnt(i, j, i == N - 3);
                // 일치하는 갯수가 0일 경우
                if (sameCnt == 0)
                {
                    // 뒤집기 수행
                    reverse(i, j);
                    cnt++;
                }
                // 일치하는 갯수가 1 or 2일 경우
                else if (sameCnt < 3)
                {
                    // A를 B로 바꿀 수 없는 경우이기 때문에 -1 반환
                    return -1;
                }
            }
            // 다른 부분배열을 확인하는 경우
            else
            {
                // 부분배열의 A(0, 0)와 B(0, 0)가 일치하지 않을 경우
                if (arrA[i][j] != arrB[i][j])
                {
                    // 뒤집기 수행
                    reverse(i, j);
                    cnt++;
                }
            }
        }
    }
    return cnt;
}

int main()
{
    int answer, twiceN;

    cin >> N >> M;
    twiceN = N * 2;
    // 배열 입력
    for (int i = 0; i < twiceN; i++)
    {
        string inputStr;
        cin >> inputStr;
        for (int j = 0; j < M; j++)
        {
            bool inputBool = inputStr[j] == '1' ? true : false;
            if (i < N)
            {
                arrA[i][j] = inputBool;
            }
            else
            {
                arrB[i - N][j] = inputBool;
            }
        }
    }
    // 배열크기가 뒤집기를 수행하지 못하는 경우
    if (N < 3 || M < 3)
    {
        answer = checkSame(0, 0, 0);
    }
    // 뒤집기 수행 가능한 배열일 경우
    else
    {
        answer = getReverseCnt();
        // 마지막 부분배열 검사
        if (answer != -1)
        {
            answer = checkSame(N - 3, M - 3, answer);
        }
    }

    cout << answer;

    return 0;
}