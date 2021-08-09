# 레이저 통신
from collections import deque
def bfs(boards, C):
    global min_

    queue = deque()
    visited = [[W*H for _ in range(W)] for _ in range(H)]
    queue.append([C[0][0], C[0][1], -1, 0])
    visited[C[0][0]][C[0][1]] = 0

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    end_r, end_c = C[1][0], C[1][1]
    #print(visited)
    while queue:
        r, c, pre_dir, count = queue.popleft()
        if r == end_r and c == end_c:
            min_ = min(min_, count)
            continue
        for idx, d in enumerate(dirs):
            nextr, nextc = r+d[0], c+d[1]
            if 0 <= nextr < H and 0 <= nextc < W and boards[nextr][nextc] != '*':
                if idx != pre_dir: next_count = count + 1 # 방향이 바꼈다는 의미니까 +1
                else: next_count = count
                if visited[nextr][nextc] >= next_count:
                    #print("check : ", (nextr, nextc), count)
                    queue.append([nextr, nextc, idx, next_count])
                    visited[nextr][nextc] = next_count
    return

if __name__ == "__main__":
    W, H = map(int, input().split())
    min_ = W*H
    boards = []
    C = []
    for i in range(H):
        temp = input()
        boards.append(temp)
        for j in range(W):
            if temp[j] == 'C':
                C.append((i, j))
    #print(boards, C)

    bfs(boards, C)
    print(min_-1)
        