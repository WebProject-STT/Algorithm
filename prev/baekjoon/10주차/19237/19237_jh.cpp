#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;
#define boardMAX 20
#define sharkMAX 401

int N, M, k;
// 이동하려는 상어의 위치, 번호 저장하는 큐와 이동한 상어의 위치, 번호 저장하는 큐
queue<vector<int>> shark, movedShark;
// 각 좌표별 냄새를 뿌린 상어의 번호, 남은 냄새를 저장하는 배열
int sharkNum[boardMAX][boardMAX], smell[boardMAX][boardMAX];
// 상어별 현재방향과 방향별 우선순위 저장
int sharkDirection[sharkMAX], sharkPriority[sharkMAX][5][4];
int moveNum[5][2] = {{0, 0}, {-1, 0}, {1, 0}, {0, -1}, {0, 1}};

// 냄새 감소
void decreaseSmell()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // 냄새가 1일 경우
            if (smell[i][j] == 1)
            {
                // 냄새가 없어지면서 상어의 정보도 없어짐
                sharkNum[i][j] = 0;
                smell[i][j] = 0;
            }
            else if (smell[i][j] > 1)
            {
                smell[i][j]--;
            }
        }
    }
}
// 상어 이동
void moveShark()
{
    while (!shark.empty())
    {
        vector<int> current = shark.front();
        int currentX = current[0];
        int currentY = current[1];
        int currentNum = current[2];
        int nextX = -1, nextY = -1, nextDirection = -1;
        shark.pop();
        // 인접한 칸 중에 냄새가 없는 칸이 있는지 확인 (우선순위로 확인)
        for (int i = 0; i < 4; i++)
        {
            int tempDirection = sharkPriority[currentNum][sharkDirection[currentNum]][i];
            int tempX = currentX + moveNum[tempDirection][0];
            int tempY = currentY + moveNum[tempDirection][1];
            if (tempX >= 0 && tempX < N && tempY >= 0 && tempY < N && smell[tempX][tempY] == 0)
            {
                nextX = tempX, nextY = tempY, nextDirection = tempDirection;
                break;
            }
        }
        // 인접한 칸 중 냄새없는 칸이 없다면
        if (nextX == -1)
        {
            // 인접한 칸 중 본인 냄새가 나는 칸 있는지 확인 (우선순위로 확인)
            for (int i = 0; i < 4; i++)
            {
                int tempDirection = sharkPriority[currentNum][sharkDirection[currentNum]][i];
                int tempX = currentX + moveNum[tempDirection][0];
                int tempY = currentY + moveNum[tempDirection][1];
                if (tempX >= 0 && tempX < N && tempY >= 0 && tempY < N && sharkNum[tempX][tempY] == currentNum)
                {
                    nextX = tempX, nextY = tempY, nextDirection = tempDirection;
                    break;
                }
            }
        }
        // 상어는 이동했으므로 방향 변경
        sharkDirection[currentNum] = nextDirection;
        // 이동한 상어 큐에 정보 넣음
        movedShark.push({nextX, nextY, currentNum});
    }
}
// 한 칸에 상어는 한마리만 남기고 상어의 위치를 저장하고 냄새를 퍼뜨림
void findShark()
{
    while (!movedShark.empty())
    {
        vector<int> current = movedShark.front();
        int currentX = current[0];
        int currentY = current[1];
        int currentNum = current[2];
        movedShark.pop();
        // 해당 칸에 상어의 흔적이 없거나 현재 상어의 우선순위가 더 높을 경우
        if (sharkNum[currentX][currentY] == 0 || sharkNum[currentX][currentY] >= currentNum)
        {
            // 냄새 퍼뜨림
            smell[currentX][currentY] = k;
            // 해당 칸에 현재 상어 흔적 남김
            sharkNum[currentX][currentY] = currentNum;
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // 새로 이동한 상어의 정보 넣음
            if (smell[i][j] == k)
            {
                shark.push({i, j, sharkNum[i][j]});
            }
        }
    }
}

int main()
{
    int time = 0, boardInput, direction, priority;

    cin >> N >> M >> k;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> boardInput;
            if (boardInput > 0)
            {
                // 상어 번호 저장
                sharkNum[i][j] = boardInput;
                // 이동하려는 상어 정보 저장
                shark.push({i, j, boardInput});
                // 냄새 퍼뜨림
                smell[i][j] = k;
            }
        }
    }
    // 상어별 현재 방향 입력
    for (int i = 1; i <= M; i++)
    {
        cin >> direction;
        sharkDirection[i] = direction;
    }
    // 상어별 방향별 우선순위 입력
    for (int i = 1; i <= M; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                cin >> priority;
                sharkPriority[i][j][k] = priority;
            }
        }
    }

    while (true)
    {
        if (shark.size() == 1)
        {
            break;
        }
        if (time == 1000)
        {
            time = -1;
            break;
        }
        moveShark();
        decreaseSmell();
        findShark();
        time++;
    }

    cout << time;
    return 0;
}