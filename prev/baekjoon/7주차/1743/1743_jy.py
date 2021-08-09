# 음식물피하기
import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
grid = [[0 for _ in range(M)] for _ in range(N)]
visited = [i[:] for i in grid]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    grid[r-1][c-1] = 1

dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_ = 0

# BFS
def BFS(x, y):
    queue = deque()
    queue.append((x, y))
    count = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            next_r, next_c = r+dir_[i][0], c+dir_[i][1]
            if 0 <= next_r < N and 0 <= next_c < M:
                if grid[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = 1
                    queue.append((next_r, next_c))
                    count += 1
    return count

for x in range(N):
    for y in range(M):
        if grid[x][y]:
            visited[x][y] = 1
            re = BFS(x, y)
            max_ = max(max_, re)
            
print(max_)




