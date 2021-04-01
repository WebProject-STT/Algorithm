# 음식물 피하기
import sys
from collections import deque

def bfs(r, c, cnt):
    q = deque()
    q.append((r, c))
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계 방향
    while q :
        r, c = q.popleft()
        for i in range(4) :
            nr  = r + d[i][0]
            nc  = c + d[i][1]
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 1 and visit[nr][nc] == 0 :
                visit[nr][nc] = 1
                cnt += 1
                q.append((nr, nc))
    return cnt



if __name__ == "__main__" :
    input = sys.stdin.readline

    n, m, k = map(int, input().split()) # 세로, 가로, 음식물
    matrix = [[0] * m  for _ in range(n)]
    trash = []
    for _ in range(k) :
        r, c = map(int, input().split())
        r -= 1
        c -= 1
        matrix[r][c] = 1
        trash.append((r, c))

    visit = [[0] * m  for _ in range(n)]

    cnt = 0
    for i in range(k) :
        r, c = trash[i]
        if visit[r][c] == 0 :
            cnt = max(cnt, bfs(r, c, 0))
    
    print(cnt)