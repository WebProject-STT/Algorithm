#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;
// 다리 위에 올라간 트럭들의 무게 합, 트럭 갯수, 현재 트럭 인덱스
int sumWeight = 0, curCnt = 0, curIndex = 0;
// 입력받은 트럭의 무게를 저장하는 벡터
vector<int> inputTruck;
// 다리를 건너간 트럭을 저장하는 큐
queue<int> completedTruck;
// 다리 위에 올라간 트럭의 무게와 다리 위에 있었던 시간을 저장하는 큐
queue<pair<int, int>> truckBridge;

int main()
{
    int N, W, L, time = 0;

    cin >> N >> W >> L;
    inputTruck.resize(N);

    for (int i = 0; i < N; i++)
    {
        cin >> inputTruck[i];
    }
    // 트럭이 모두 다리를 건너기 전까지 반복문 실행
    while (completedTruck.size() != inputTruck.size())
    {
        int size = truckBridge.size();
        // 시간이 흐름에 따라 다리 위의 트럭은 앞으로 전진
        for (int i = 0; i < size; i++)
        {
            int curWeight = truckBridge.front().first;
            int curTime = truckBridge.front().second;
            truckBridge.pop();
            // 트럭이 다리를 건너면
            if (curTime == W)
            {
                sumWeight -= curWeight;
                curCnt--;
                completedTruck.push(curWeight);
            }
            else
            {
                curTime++;
                truckBridge.push({curWeight, curTime});
            }
        }
        // 트럭을 다리에 올림
        if (curIndex < N && curCnt < W && sumWeight + inputTruck[curIndex] <= L)
        {
            truckBridge.push({inputTruck[curIndex], 1});
            sumWeight += inputTruck[curIndex];
            curIndex++;
            curCnt++;
        }
        time++;
    }

    cout << time;

    return 0;
}