#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
/*
    생각의 전환..!!
    S에서 T를 만드는게 아니라 T를 S로 만드는게 가능한지 확인
    T의 마지막 원소를 확인하며 기존에 행한 연산을 하나씩 취소함
*/
int main() {
	string S, T;

	cin >> S >> T;
    // T가 S보다 길 경우
	while (S.length() < T.length()) {
        // T의 마지막 원소
		char end = T[T.length() - 1];
        // end가 A이든 B이든 마지막 원소는 지워야 함
        T.pop_back();
        // end가 B이면 문자열 디Zㅣ버Zㅕ야 함
		if(end == 'B') {
			reverse(T.begin(), T.end());
		}
	}
    // T와 S가 같다면 S는 T로 만들 수 있는 것이므로 1 출력, 아니면 0 출력
	S == T ? cout << 1 : cout << 0;
	return 0;
}