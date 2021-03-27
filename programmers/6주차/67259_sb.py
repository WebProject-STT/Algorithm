# 경주로건설

from collections import deque

def solution(board):
    n = len(board)
    matrix = [[0] * n for _ in range(n)] # 금액 저장을 위한 matrix
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계 방향
    q = deque() # 경로 기록을 위한 queue
    
    # (0, 0) 위치에서 시작할 때 갈 수 있는 위치는 우, 하
    q.append((0, 0, 1, 0)) # r, c, front, coin
    q.append((0, 0, 2, 0)) # r, c, front, coin
    
    while q : # 모든 경로에 대해 다 탐색할 동안 수행
        r, c, front, coin = q.popleft()
        
        for i in range(4) :
            nr, nc = r + d[i][0], c + d[i][1] # 다음으로 이동할 위치
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                ncoin = coin + 100 # 이동 경로에 대해 100원 더해줌
                if i != front : ncoin += 500 # 방향이 전환되므로 코너임 -> 500원 더해줌
                if matrix[nr][nc] == 0 or matrix[nr][nc] >= ncoin : # 처음 가는 경로 or 금액이 최소가 되는 경로
                    matrix[nr][nc] = ncoin
                    q.append((nr, nc, i, ncoin)) # 경로에 대한 정보 추가
    
    return matrix[-1][-1]