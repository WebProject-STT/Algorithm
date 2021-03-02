#include <iostream>
#include <string>
#include <string.h>
#include <math.h>
using namespace std;
#define MAX 10001
// 무한루프 여부를 확인하기 위한 배열
bool check[MAX] = {false};
// 소수 판별 함수
bool isPrimeNumber(int n)
{
    // sqrt는 n의 제곱근을 구해줌
    for (int i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}
// 행복한 소수 판별하는 함수
bool isHappyPrimeNumber(int n)
{
    int total = 0;
    string strN = to_string(n);
    // n이 1이면 true 리턴
    if (n == 1)
    {
        return true;
    }
    // 무한루프를 돌고 있다면 false 반환
    if (check[n])
    {
        return false;
    }
    // n 방문 표시
    check[n] = true;
    for (auto elem : strN)
    {
        // char형의 elem을 int형으로 변환
        int current = elem - '0';
        total += current * current;
    }
    return isHappyPrimeNumber(total);
}

int main()
{
    int P, index, num;
    int *primeNumber;
    string *answer;

    cin >> P;
    primeNumber = new int[P + 1];
    answer = new string[P + 1];

    for (int i = 1; i <= P; i++)
    {
        int cnt = 0;
        cin >> index >> num;
        primeNumber[i] = num;
        // num이 7보다 작거나 소수가 아니라면 answer에 NO를 넣음
        if (num < 7 || !isPrimeNumber(num))
        {
            answer[i] = "NO";
            continue;
        }
        // 행복한 소수 여부 확인
        if (isHappyPrimeNumber(num))
        {
            answer[i] = "YES";
        }
        else
        {
            answer[i] = "NO";
        }
        // 배열 초기화
        memset(check, false, MAX);
    }

    for (int i = 1; i <= P; i++)
    {
        cout << i << " " << primeNumber[i] << " " << answer[i] << '\n';
    }

    return 0;
}