# 뱀
import sys
from collections import deque
N = int(sys.stdin.readline())
grid = [[0 for _ in range(N)] for _ in range(N)]
grid[0][0] = 1
A = int(sys.stdin.readline())
for _ in range(A):
    a, b = map(int, sys.stdin.readline().split())
    grid[a-1][b-1] = 2
C = int(sys.stdin.readline())
snake = []
for _ in range(C):
    a, b = sys.stdin.readline().split()
    snake.append((int(a), b))

snake_info = deque()

dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북
# 동(0) -> 북(3), 서(1) -> 남(2), 남(2) -> 동(0), 북(3) -> 서(1)
change_dir_L = (3, 2, 0, 1)
# 동(0) -> 남(2), 서(1) -> 북(3), 남(2) -> 서(1), 북(3) -> 동(0)
change_dir_R = (2, 3, 1, 0)

time = 1
cur_dir, cur_r, cur_c = 0, 0, 0
s_idx, s_len = 0, len(snake)
snake_info.append((0, 0))

    
while True:
    # x 초가 끝난 후 방향 바꾸는 거임 +1 필수
    if s_idx <= s_len-1 and snake[s_idx][0]+1 == time: # 방향 바꾸기
        if snake[s_idx][1] == 'L':
            cur_dir = change_dir_L[cur_dir]
        else:
            cur_dir = change_dir_R[cur_dir]
        s_idx += 1

    
    # 뱀이 하는 행동
    # 1. 먼저 뱀은 몸길이 늘려 다음칸에 위치시킨다
    next_r, next_c = cur_r + dir_[cur_dir][0], cur_c + dir_[cur_dir][1]
    if 0 <= next_r < N and 0 <= next_c < N and grid[next_r][next_c] != 1: # 범위 안에 있고 내 몸 아니면
        if grid[next_r][next_c] != 2: # 사과 없으면 -> 꼬리 제거
            tail_r, tail_c = snake_info.popleft()
            grid[tail_r][tail_c] = 0
        snake_info.append((next_r, next_c))
        grid[next_r][next_c] = 1
        cur_r, cur_c = next_r, next_c
    else:
        break
    time += 1
print(time)