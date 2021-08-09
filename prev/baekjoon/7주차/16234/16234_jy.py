# 인구 이동 -> PyPy3만 통과
import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    people, p_count = 0, 0
    temp_visited = []
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            next_r, next_c = r+dir_[i][0], c+dir_[i][1]
            if 0 <= next_r < N and 0 <= next_c < N:
                if not visited[next_r][next_c] and L <= abs(countries[next_r][next_c]-countries[r][c]) <=R:
                    visited[next_r][next_c] = 1
                    queue.append((next_r, next_c))
                    temp_visited.append((next_r, next_c))
                    people += countries[next_r][next_c]
                    p_count += 1
                    
    if p_count: return (temp_visited, people//p_count)
    else: return False


if __name__ == "__main__":
    count = 0 # 인구이동 횟수

    while True:
        check = False # 인구 이동 했는지 check
        visited = [[0 for _ in range(N)] for _ in range(N)] # BFS
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    temp = BFS(i, j) # 현재 위치에서 BFS로 갈 수 있는 주변 국가 모두 탐색
                    if temp: 
                        check=True # 있으면 CHECK
                        for r, c in temp[0]: countries[r][c] = temp[1]
        if not check:
            print(count)
            break
        count += 1
    