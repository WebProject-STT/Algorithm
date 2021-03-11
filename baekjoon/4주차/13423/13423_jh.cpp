#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// 양쪽으로 center와 같은 거리에 있는 정점의 경우의 수를 반환하는 함수
int findSameDistance(vector<int> dots, int center)
{
    // 경우의 수 저장하는 변수
    int cnt = 0;
    // 양쪽 끝에서부터 정점 찾기 위해 변수 설정
    int leftIndex = 0, rightIndex = dots.size() - 1;
    while (leftIndex < rightIndex)
    {
        int leftDistance = center - dots[leftIndex];
        int rightDistance = dots[rightIndex] - center;
        if (leftDistance == rightDistance)
        {
            cnt++;
            leftIndex++;
            rightIndex--;
        }
        else if (leftDistance > rightDistance)
        {
            leftIndex++;
        }
        else
        {
            rightIndex--;
        }
    }
    return cnt;
}

int main()
{
    int T, N;
    vector<int> answer;

    cin >> T;
    answer.assign(T, 0);

    for (int i = 0; i < T; i++)
    {
        vector<int> dots;
        cin >> N;
        dots.resize(N);
        for (int j = 0; j < N; j++)
        {
            cin >> dots[j];
        }
        sort(dots.begin(), dots.end());
        // 양쪽 끝 점들은 가운데점이 될 수 없으므로 반복문에서 제외
        for (int j = 1; j < N - 1; j++)
        {
            answer[i] += findSameDistance(dots, dots[j]);
        }
    }

    for (auto elem : answer)
    {
        cout << elem << '\n';
    }

    return 0;
}