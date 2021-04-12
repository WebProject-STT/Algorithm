# 인구이동
import sys
from collections import deque

# 인구 이동
def bfs(i, j) :
    q = deque()
    q.append((i, j))
    pepole, count = 0, 0 # 총 인구수, 칸의 개수
    temp = [] # 경계가 없는 위치 모음
    while q :
        r, c = q.popleft()
        for i in range(4) :
            nr, nc = r + d[i][0], c + d[i][1]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and L <= abs(matrix[r][c] - matrix[nr][nc]) <= R :
                visited[nr][nc] = 1
                q.append((nr, nc))
                pepole += matrix[nr][nc]
                count += 1
                temp.append((nr, nc))
    if count :
        for i, j in temp :
            matrix[i][j] = pepole//count
        return 1
    return 0

if __name__=="__main__" :
    input = sys.stdin.readline

    N, L, R = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)] # 각 나라의 인구수
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계 방향

    cnt = 0 # 총 이동 수

    while True :
        check = 0
        visited = [[0] * N for _ in range(N)]
        for i in range(N) :
            for j in range(N) :
                if visited[i][j] == 0:
                    if bfs(i, j) :
                        check = 1
        if check == 0:
            break
        cnt += 1

    print(cnt)