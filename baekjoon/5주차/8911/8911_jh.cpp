#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    // 상, 하, 좌, 우 이동할 때 쓰일 변수
    int directionNum[4][2] = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
    vector<int> answer;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        // 현재 거북이의 위치와 이동 방향
        int curX = 0, curY = 0, curDirection = 0;
        // X, Y 좌표의 최댓값과 최소값
        int minX = 0, maxX = 0, minY = 0, maxY = 0;
        string turtleMove;
        cin >> turtleMove;
        for (auto elem : turtleMove)
        {
            // 입력값이 L이나 R일 경우 이동 방향만 변경
            if (elem == 'L')
            {
                curDirection = (curDirection + 1) % 4;
            }
            else if (elem == 'R')
            {
                curDirection = (curDirection + 3) % 4;
            }
            // 입력값이 F나 B일 경우 이동 방향에 맞춰 이동
            else if (elem == 'F')
            {
                curX += directionNum[curDirection][0];
                curY += directionNum[curDirection][1];
            }
            else
            {
                curX -= directionNum[curDirection][0];
                curY -= directionNum[curDirection][1];
            }
            // X, Y 최댓값과 최솟값 갱신
            minX = min(minX, curX);
            maxX = max(maxX, curX);
            minY = min(minY, curY);
            maxY = max(maxY, curY);
        }
        // 거북이 이동 영역 포함하는 직사각형 넓이 저장
        answer.push_back((maxX - minX) * (maxY - minY));
    }

    for (auto elem : answer)
    {
        cout << elem << '\n';
    }

    return 0;
}