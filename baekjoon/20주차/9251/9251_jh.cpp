#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
/*
    입력: ACAYKP(A), CAPCAK(B)
    DP[i][j] => A[0] ~ A[i-1] 문자열과 B[0] ~ B[i-1] 문자열 사이의 LCS(최장 공통 부분 수열) 최대 길이
    DP 배열은 다음과 같음

       0  A  C  A  Y  K  P
    0  0  0  0  0  0  0  0
    C  0  0  1  1  1  1  1
    A  0  1  1  2  2  2  2
    P  0  1  1  2  2  2  3 
    C  0  1  2  2  2  2  3
    A  0  1  2  3  3  3  3 
    K  0  1  2  3  3  4  4

    1. A[i]와 B[i]가 같으면 더 긴 공통 부분 수열이 더 존재한다는 것
        => 현재 원소들을 비교하기 이전의 긴 공통 부분 수열 길이에 1을 더해야 함
        => DP[i][j] = DP[i-1][j-1] + 1
    2. A[i]와 B[i]가 다르면 더 긴 공통 부분 수열이 존재하지 않는다는 것
        => 이전 길이 값들 중 최대값을 구해야 함
        => DP[i][j] = max(DP[i-1][j], DP[i][j-1])
*/
int main() {
	string input1, input2;
	vector<vector<int>> dp;
	int size1, size2;

	cin >> input1 >> input2;
	size1 = input1.size() + 1;
	size2 = input2.size() + 1;

	dp.assign(size2, vector<int>(size1, 0));

	for (int i = 1; i < size2; i++) {
		char temp2 = input2[i - 1];
		for (int j = 1; j < size1; j++) {
			char temp1 = input1[j - 1];
			if (temp2 == temp1) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
			}
			else {
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
			}
		}
	}

	cout << dp[size2 - 1][size1 - 1];
	return 0;
}