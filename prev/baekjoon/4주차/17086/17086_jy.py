# 아기상어2
from collections import deque
queue = deque([])
n, m = map(int, input().split())
visited = []

for i in range(n):
    t = list(map(int, input().split()))
    visited.append(t)
    for j in range(m):
        if t[j]: 
            queue.append((i, j))


dir_r = [-1, 1, 0, 0, -1, 1, -1, 1]
dir_c = [0, 0, -1, 1, -1, 1, 1, -1]

max_ = 0

def check(next_r, next_c): 
    return 0 <= next_r < n and 0 <= next_c < m
  
def bfs():
    global max_
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(8):
            next_r, next_c = cur_r + dir_r[i], cur_c + dir_c[i]
            if check(next_r, next_c) and not visited[next_r][next_c]:
                visited[next_r][next_c] += (visited[cur_r][cur_c] + 1)
                queue.append((next_r, next_c))
                max_ = max(max_, visited[next_r][next_c])
bfs()
print(max_-1)