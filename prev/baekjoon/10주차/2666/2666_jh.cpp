#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define MAX 1e9
// 완전탐색으로 풀이
// (핵심은 완전탐색과 문의 이동 횟수는 열린 문과 현재 문 차이의 절댓값이라는 것)
// 벽장개수와 사용할 벽장의 개수
int N, length;
// (문은 2개 열려있음) 첫번째, 두번째 열린 문의 번호와 정답
int firstDoor, secondDoor, answer = MAX;
vector<int> order;
// 조합 => 완전탐색
void dfs(int currentIdx, int total)
{
    int add;
    // 재귀가 종료된 뒤 원래 열려있던 문의 번호를 저장하기 위함
    int tempFirstDoor = firstDoor, tempSecondDoor = secondDoor;
    // 모든 원소 탐색하면
    if (currentIdx == length)
    {
        // 문의 이동 횟수 최솟값 구함
        answer = min(answer, total);
        return;
    }
    // 이동횟수 구함
    add = abs(order[currentIdx] - firstDoor);
    // 현재 문이 열리게 되므로 첫번째로 열린 문의 번호 변경
    firstDoor = order[currentIdx];
    dfs(currentIdx + 1, total + add);
    // 재귀가 종료된 뒤에는 원래 문의 번호 대입
    firstDoor = tempFirstDoor;
    add = abs(order[currentIdx] - secondDoor);
    secondDoor = order[currentIdx];
    dfs(currentIdx + 1, total + add);
    secondDoor = tempSecondDoor;
}
int main()
{
    int orderNum;

    cin >> N;

    cin >> firstDoor;
    cin >> secondDoor;

    cin >> length;

    for (int i = 0; i < length; i++)
    {
        cin >> orderNum;
        order.push_back(orderNum);
    }

    dfs(0, 0);

    cout << answer;

    return 0;
}

/* 처음에 시도한 풀이
   그리디하게 풀릴거라 생각했는데 그렇지 않았음..
   현재 상황에서 최선의 선택이 이후에도 최선의 결과를 가져올거라는
   보장이 없기때문에 그리디로 풀면 안됨
int N;
vector<bool> openCupboard;

void moveDoor(int current, bool isMoveRight, int moveCnt) {
	int start, end;
	if (isMoveRight) {
		start = current + 1;
		end = current + moveCnt;
	}
	else {
		start = current - moveCnt;
		end = current - 1;
	}
	openCupboard[current] = true;
	for (int i = start; i <= end; i++) {
		openCupboard[i] = false;
	}
}

int getMoveCnt(int current) {
	bool isMoveRight, canMoveLeft = true, canMoveRight = true;
	int leftCloseCnt = 0, rightCloseCnt = 0, moveCnt;
	for (int i = current; i >= 1; i--) {
		if (openCupboard[i]) {
			break;
		}
		if (!openCupboard[i]){
			leftCloseCnt++;
		}
		if (i == 1) {
			canMoveLeft = false;
		}
	}
	for (int i = current; i <= N; i++) {
		if (openCupboard[i]) {
			break;
		}
		if (!openCupboard[i]) {
			rightCloseCnt++;
		}
		if (i == N) {
			canMoveRight = false;
		}
	}
	if (canMoveLeft && leftCloseCnt <= rightCloseCnt) {
		isMoveRight = false;
		moveCnt = leftCloseCnt;
	}
	else {
		isMoveRight = true;
		moveCnt = rightCloseCnt;
	}
	cout << moveCnt << '\n';
	if (moveCnt != 0) {
		moveDoor(current, isMoveRight, moveCnt);
	}
	return moveCnt;
}

int main()
{
	vector<int> order;
	int length, openNum, orderNum, answer = 0;

	cin >> N;
	openCupboard.assign(N + 1, false);

	for (int i = 0; i < 2; i++) {
		cin >> openNum;
		openCupboard[openNum] = true;
	}

	cin >> length;

	for (int i = 0; i < length; i++) {
		cin >> orderNum;
		order.push_back(orderNum);
	}

	for (auto elem : order) {
		answer += getMoveCnt(elem);
	}

	cout << answer;

	return 0;
}*/