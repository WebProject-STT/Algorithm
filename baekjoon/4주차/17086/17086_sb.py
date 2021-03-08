# 아기 상어2
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 칸의 전체 크기
metrix = [list(map(int, input().split())) for _ in range(n)] # 칸에 대한 정보
dx = [-1, -1, -1, 0, 0, 1, 1, 1] # 현재 위치에서 8뱡향으로의 x
dy = [-1, 0, 1, -1, 1, -1, 0, +1] # 현재 위치에서 8방향으로의 y
q = deque([])

for i in range(n) :
    for j in range(m) :
        if metrix[i][j] :
            q.append([i, j])

cnt = 0 # 가장 큰 값 저장
while q :
    i, j = q.popleft()
    for l in range(8) :
        x = i + dx[l]
        y = j + dy[l]
        if 0 <= x < n and 0 <= y < m and metrix[x][y] == 0:
            metrix[x][y] = metrix[i][j] + 1
            q.append([x, y])
            cnt = max(cnt, metrix[x][y])

print(cnt - 1) # 아기상어 표시가 1이어서 안전거리+1에 대한 정보를 가지고 있으므로 결과 출력 시 1 빼줌