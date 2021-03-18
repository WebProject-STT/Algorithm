#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
// k개의 디딤돌 숫자가 모두 0이 되는 구간의 존재 유무 확인
bool findZero(vector<int> stones, int k, int num)
{
    int cnt = 0;
    for (auto elem : stones)
    {
        // 디딤돌 숫자가 num보다 작거나 같다 => 0이다
        if (elem <= num)
        {
            cnt++;
            // k개의 디딤돌 숫자가 연속으로 0이면 true 반환
            if (cnt == k)
            {
                return true;
            }
        }
        // 디딤돌 숫자 0 아니면 cnt 변수 초기화
        else
        {
            cnt = 0;
        }
    }
    // 구간 없으면 false 반환
    return false;
}

int solution(vector<int> stones, int k)
{
    int leftNum = 1, rightNum = *max_element(stones.begin(), stones.end());
    int answer = rightNum;
    // 이분탐색 실시
    // 탐색 대상은 징검다리를 건널 수 있는 사람의 최대 수!
    while (leftNum <= rightNum)
    {
        int halfNum = (leftNum + rightNum) / 2;
        // 구간 찾으면
        if (findZero(stones, k, halfNum))
        {
            // halfNum의 최소값이 정답
            answer = halfNum;
            // halfNum 기준으로 왼쪽 탐색
            rightNum = halfNum - 1;
        }
        else
        {
            // halfNum 기준으로 오른쪽 탐색
            leftNum = halfNum + 1;
        }
    }

    return answer;
}

// 첫번째로 시도한 방법, 효율성 13번만 틀림 짜증나!!!!
// int solution(vector<int> stones, int k) {
//     int answer = 200000000, maxNum;
//     int size = stones.size();
//     auto maxIndex = stones.end();

//     for(int i = 0; i <= size - k; i++) {
//         if(maxIndex >= stones.begin() + i && maxIndex < stones.begin() + i + k) {
//             if (maxNum >= stones[i + k - 1])
//                 continue;
//             else {
//                 maxIndex = stones.begin() + i + k - 1;
//             }
//         }
//         else {
//             maxIndex = max_element(stones.begin() + i, stones.begin() + i + k);
//         }
//         maxNum = *maxIndex;
//         answer = min(answer, maxNum);
//     }

//     return answer;
// }