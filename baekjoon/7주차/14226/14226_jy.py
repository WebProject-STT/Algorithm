# 이모티콘
import sys
from collections import deque
S = int(sys.stdin.readline())
queue = deque()
queue.append((1, 0, 0)) # 화면, 클립보드, 초
visited = [[0]*(S+1) for _ in range(S+1)]
min_ = sys.maxsize

while queue:
    screen, clip, time = queue.popleft()
    if screen == S: 
        #min_ = min(min_, time)
        print(time)
        break

    # 1. 화면에 있는 이모티콘 모두 복사 + 클립보드에 저장
    if screen < S and not visited[screen][screen]:
        visited[screen][screen] = 1
        queue.append((screen, screen, time+1))
    # 2. 클립보드에 있는거 모두 화면에 복사
    if screen+clip <= S and clip != 0 and not visited[screen+clip][clip]:
        visited[screen+clip][clip] = 1
        queue.append((screen+clip, clip, time+1))
    # 3. 화면에 있는 이모티콘 삭제(한개)
    if screen-1 >= 0 and not visited[screen-1][clip]:
        visited[screen-1][clip] = 1
        queue.append((screen-1, clip, time+1))