# 돌다리
from collections import deque

a, b, n, m = map(int, input().split())
d = [1, -1, a, b, -a, -b, a, b]
limit = 100001

cnt = [0] * limit # 각 위치에서의 방문 횟수 저장을 위한 list
visit = [0] * limit # 최소 이동 횟수이므로 이동한 위치에 또 이동할 필요 X
q = deque() # while문 생성을 위해 사용할 queue

q.append(n) # 동규의 현재 위치 추가

while q : # 이동할 수 있는 모든 경로에 대한 방문 횟수 계산
    cur = q.popleft() # 출발 위치
    for i in range(8) :
        if i < 6 :
            move = cur + d[i] # 예상 이동 경로 계산
            if 0 <= move < limit and visit[move] == 0:
                cnt[move] = cnt[cur] + 1 # 방문 횟수 추가
                q.append(move) # 예상 이동 경로 추가
                visit[move] = 1
        else :
            move = cur * d[i] # 예상 이동 경로 계산
            if 0 <= move < limit and visit[move] == 0:
                cnt[move] = cnt[cur] + 1 # 방문 횟수 추가
                q.append(move) # 예상 이동 경로 추가
                visit[move] = 1 

print(cnt[m])
