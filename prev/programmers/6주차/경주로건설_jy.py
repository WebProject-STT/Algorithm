# 경주로 건설
from collections import deque
def solution(board):
    N = len(board)
    dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 남 북 동 서
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 0
    queue = deque()
    # queue[0] = 상,하,좌,우 표시 / queue[1][2] = (r, c) / queue[3] = cost
    # 초기 세팅
    queue.append((2, 0, 0, 0))  # 오른쪽으로 가는 경우
    queue.append((0, 0, 0, 0)) # 아래로으로 가는 경우
    while queue:
        pre_dir, cur_r, cur_c, cost = queue.popleft()
        for i in range(4):
            next_r, next_c = cur_r+dir_[i][0], cur_c+dir_[i][1]
            if 0 <= next_r < N and 0 <= next_c < N and board[next_r][next_c] != 1:
                next_cost = cost + 100 if i == pre_dir else cost + 600
                if visited[next_r][next_c] == -1 or visited[next_r][next_c] >= next_cost:
                    queue.append((i, next_r, next_c, next_cost))
                    visited[next_r][next_c] = next_cost
    return visited[-1][-1]
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))