#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
/*  
    비교 횟수가 작으려면 작은 수를 여러번 더해야함
    => 우선순위 큐 사용 (오름차순 정렬)
    앞에서 비교한 횟수를 계속 더해나가야 하기 때문에
    더한 횟수를 큐에 다시 넣어줘야 함
*/
int getCnt(priority_queue<int, vector<int>, greater<int>> add, int total) {
    // add의 크기가 1보다 클 경우
    // (아직 비교가 다 안 끝났을 경우)
	while (add.size() > 1) {
		int num1 = add.top();
		add.pop();
		int num2 = add.top();
		add.pop();
        // 큐 앞의 두 숫자를 더함
		int addNum = num1 + num2;
        // 더한걸 다시 add에 넣어줌
		add.push(addNum);
        // 총 횟수에 더 해줌
		total += addNum;
	}
	return total;
}

int main() {
	int N, num;
    // 오름차순 정렬하는 우선순위 큐 선언
	priority_queue<int, vector<int>, greater<int>> add;
	cin >> N;
	while (N--) {
		cin >> num;
		add.push(num);
	}
	cout << getCnt(add, 0);
	return 0;
}