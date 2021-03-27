# 뱀
import sys
from collections import deque
inp = sys.stdin.readline

n = int(inp()) # 보드 크기
matrix = [[0] * n for _ in range(n)] # 보드 생성

k = int(inp()) # 사과 개수
for _ in range(k) :
    r, c = map(int, inp().split())
    matrix[r-1][c-1] = 1 # 사과 위치는 1로 표시

l = int(inp()) # 뱀의 방향 변환 횟수
moves = []
for _ in range(l) :
    x, c = inp().split()
    moves.append((int(x), c)) # 방향 전환 정보
m_idx = 0 # 방향 전환 정보에 대한 index

# matrix[0][0] = 2 # 뱀의 현재 위치 (정확히는 머리에 대한 위치)
d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계 방향
f = 1 # 뱀의 머리 위치
q = deque() # 뱀의 전체 위치에 대한 정보 저장 (몸 길이 증가에 따라 늘어남)
t = 0 # 시간에 대한 정보
r, c = 0, 0 # 현재 뱀의 머리 위치
q.append((r, c)) # 뱀의 처음 위치 저장

while True :
    t += 1 # 시간 추가

    # 뱀 이동
    r += d[f][0]
    c += d[f][1]
    if (r, c) in q : # 머리가 몸통 중 일부와 만남
        break
    q.append((r, c)) # 이동한 방향의 머리 위치 추가
    if 0 <= r < n and 0 <= c < n :
        if matrix[r][c] != 1 : # 사과가 존재하지 않음
            q.popleft() # 꼬리 위치에 대한 정보 제거 (뱀의 몸 길이 유지)
        if matrix[r][c] == 1 : # 사과가 존재함
            matrix[r][c] = 0 # 뱀이 사과 먹음 (뱀의 몸은 길어짐)
    else : # 벽에 부딪힘
        break

    # 방향 전환
    if m_idx < l and t == moves[m_idx][0] : # x초 후
        if moves[m_idx][1] == 'L' : # 왼쪽
            f = (f + 3) % 4
        else : # 오른쪽
            f = (f + 1) % 4
        m_idx += 1

print(t) # 시간에 대한 정보 출력