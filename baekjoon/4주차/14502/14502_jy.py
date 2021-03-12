# 연구소
import sys
from collections import deque
import copy
N, M = map(int,sys.stdin.readline().split())
grids = []
# 조합할 위치들 => 0인 위치
temp_visited, temp_q = [], []
max_ = 0
for i in range(N):
    temp = list(map(int,sys.stdin.readline().split()))
    grids.append(temp)
    for j in range(M):
        if temp[j] == 1: continue
        if not temp[j]: 
            temp_visited.append((M*i)+j) # (1, 3) = 가로//2, 가로% 로 구할 수 있음
            continue
        if temp[j] == 2: temp_q.append((i, j)) # 2의 정보 저장
num = len(temp_visited)
visited = [0]*num

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def spread(copy_grid): # SPREAD는 BFS로 
    queue = deque(temp_q)
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            next_r, next_c = row+dx[i], col+dy[i]
            if 0 <= next_r < N and 0 <= next_c < M and not copy_grid[next_r][next_c]:
                queue.append((next_r, next_c))
                copy_grid[next_r][next_c] = 2
    count = 0
    for row in copy_grid:
        count += row.count(0)
    return count
                
def find_combi(cur_num, last_num):
    global max_
    if cur_num == 2:
        copy_grid = copy.deepcopy(grids)
        for i in range(num):
            if visited[i]:
                a, b = temp_visited[i]//M, temp_visited[i]%M
                copy_grid[a][b] = 1
        max_ = max(spread(copy_grid), max_)
        return
    
    for i in range(last_num+1, num):
        if not visited[i]: 
            visited[i] = 1
            find_combi(cur_num+1, i)
            visited[i] = 0

# dfs로 조합 구하기
for i in range(num):
    visited[i] = 1
    find_combi(0, i)
    visited[i] = 0

print(max_)
