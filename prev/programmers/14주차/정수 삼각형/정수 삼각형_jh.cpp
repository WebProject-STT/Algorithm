#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;
/*
    정수 삼각형
    위에서 아래로 내려가며 최대값을 계산하는 문제 => dp로 풀이
    삼각형의 첫번째 열과 마지막 열은 그냥 쭉~~ 더하면 그것이 최대값
    가운데 열들은 위 칸의 왼쪽 대각선, 오른쪽 대각선의 dp 값 중 최대값을 더해야 됨
*/
int solution(vector<vector<int>> triangle) {
    int answer = 0, size = triangle.size();
    vector<vector<int>> dp(size);
    // 주어진 삼각형 형태로 dp배열 초기화
    for(int i=0; i<size; i++) {
        dp[i].resize(i + 1);
    }
    dp[0][0] = triangle[0][0];
    for(int i=1; i<size; i++) {
        int rowSize = triangle[i].size();
        for(int j=0; j<rowSize; j++) {
            // 첫번째 열이거나 마지막 열일 경우에는 그냥 위 칸의 dp값과 현재 원소를 더함
            if(j == 0) {
                dp[i][j] = dp[i-1][j] + triangle[i][j];
            }
            else if(j == rowSize - 1) {
                dp[i][j] = dp[i-1][j-1] + triangle[i][j];
            }
            // 가운데 열일 경우에는
            else {
                // 위 칸의 왼쪽 or 오른쪽에 있는 값 중 최대값을 찾아 현재 원소와 더함
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) +  triangle[i][j];
            }
        }
    }
    // 마지막 행의 최대값이 정답
    answer = *max_element(dp[size - 1].begin(), dp[size - 1].end());
    return answer;
}