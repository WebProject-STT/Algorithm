# 아기 상어
import sys
from collections import deque

# 물고기를 찾는 함수
def find_fish() :
    global r, c, s, eat, t
    q = deque()
    q.append((r, c))
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = t
    can_eat = []
    while q :
        qlen = len(q)
        while qlen : # 현재 deque 안에 들어있는 값에 대해서만 확인하는 형태로 진행 (점점 범위를 넓히는 형태)
            cur_r, cur_c = q.popleft() # 아기상어의 현재 위치
            for i in range(4) :
                nr, nc = cur_r + d[i][0], cur_c + d[i][1] # 아기상어의 다음 예상 위치
                if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] <= s and visited[nr][nc] == 0 :
                    visited[nr][nc] = visited[cur_r][cur_c] + 1
                    q.append((nr, nc))
                    if 0 < matrix[nr][nc] < s :
                        can_eat.append((nr, nc))
            qlen -= 1
        if can_eat : # 먹을 수 있는 물고기 존재
            eat_r, eat_c = min(can_eat) # 조건에 해당하는 물고기 한마리
            eat += 1
            if eat == s : # 먹은 횟수가 물고기 크기와 같아짐
                eat = 0
                s += 1
            matrix[eat_r][eat_c] = 0 # 물고기를 먹고나면 0으로 바뀜
            t = visited[eat_r][eat_c] # 시간 변경
            r, c = eat_r, eat_c # 물고기 위치 변경
            return 1 # 먹고 나면 다시 처음부터 수행하기 위해 return
    return 0

if __name__=="__main__" :
    input = sys.stdin.readline

    N = int(input()) # 공간의 크기
    matrix = [] # 공간에 대한 정보를 저장할 matrix
    r, c, s, eat = 0, 0, 2, 0 # 아기상어 정보 (위치 및 크기), 아기상어의 eat 횟수
    t = 0 # 아기상어의 이동시간
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계방향
    for i in range(N) :
        temp = list(map(int, input().split()))
        matrix.append(temp)
        for j in range(N) :
            if temp[j] == 9: # 아기상어 현재 위치
                r, c = i, j
                matrix[i][j] = 0 #아기상어 공간을 0으로 변경해주기
    
    while True :
        if not find_fish() :
            break

    print(t)

'''
아기상어는 상하좌우로 인접한 한 칸씩 이동, 이동하는데 1초 걸림
아기상어의 크기는 2이며, 크기와 같은 수의 물고기를 먹을 때마다 아기상어의 크기가 커짐
아기상어는 자신의 크기보다 작은 물고기만 먹을 수 있음 => 먹고나면 해당 위치는 0으로 바뀜
크기가 큰 물고기는 먹을 수도 지나갈수도 없음
더 이상 먹을 수 있는 물고기가 없으면 엄마상어에게 도움 요청 => 종료
먹을 수 있는 물고기가 1마리면, 그 물고기를 먹으러 감
먹을 수 있는 물고기가 1마리보다 많으면, 가장 가까운 물고기를 먹음
  아기상어가 물고기를 먹으러 이동하는 칸의 수가 최솟값이어야 함
  물고기 우선순위 : 가장 위쪽, 가장 왼쪽
---
아기상어와 인접한 칸에 먹을 수 있는 물고기 찾기
    => bfs (크기가 작은 물고기 정보를 담을 필요가 있음)
위쪽, 왼쪽 물고기 먼저 먹기
    => 물고기에 대한 리스트를 정렬시키고 먹으면 될 것 같음
       위쪽이니까 행에 대해서 정렬 후, 왼쪽이니 열에 대해 정렬
'''