#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
using namespace std;
#define MAX 100
// 전형적인 bfs 문제 아주 마음 편하게 한번에 풀었다,,

bool visited[MAX][MAX];
int moveNum[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

int bfs(int m ,int n, int startX, int startY, vector<vector<int>> picture) {
    int areaSize = 1;
    queue<pair<int, int>> needVisit;
    needVisit.push({startX, startY});
    visited[startX][startY] = true;
    
    while(!needVisit.empty()) {
        int currentX = needVisit.front().first;
        int currentY = needVisit.front().second;
        needVisit.pop();
        
        for(int i=0; i<4; i++) {
            int nextX = currentX + moveNum[i][0];
            int nextY = currentY + moveNum[i][1];
            if(nextX < 0 || nextX >= m || nextY < 0 || nextY >= n
              || picture[currentX][currentY] != picture[nextX][nextY] 
              || visited[nextX][nextY]) {
                continue;
            }
            needVisit.push({nextX, nextY});
            visited[nextX][nextY] = true;
            areaSize++;
        }
    }
    // 현재 영역 크기 리턴
    return areaSize;
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int areaCnt = 0, maxAreaSize = 0;
    vector<int> answer;
    
    for(int i=0; i<m; i++) {
        for(int j=0; j<n; j++) {
            visited[i][j] = false;
        }
    }
    
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            // 현재 칸이 색칠돼있고 아직 방문하지 않았을 경우
            if(picture[i][j] != 0 && !visited[i][j]) {
                // 가장 큰 영역의 넓이 갱신
                maxAreaSize = max(maxAreaSize, bfs(m, n, i, j, picture));
                // 영역 개수 증가
                areaCnt++;
            }
        }
    }
    
    answer.push_back(areaCnt);
    answer.push_back(maxAreaSize);
    
    return answer;
}