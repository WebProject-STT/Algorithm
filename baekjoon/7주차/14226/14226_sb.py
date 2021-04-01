# 이모티콘
from collections import deque
import sys
input = sys.stdin.readline

s = int(input())
emoji = [[0] * (s + 1) for _ in range(s + 1)]
clip = 0
q = deque()
q.append((1, 0, 0)) # emoji, clip, time
result = sys.maxsize

while q :
    e, c, t = q.popleft()
    if e >= s :
        result = min(result, t)
        continue
    
    nt = t + 1
    if emoji[e][e] > nt or emoji[e][e] == 0 : # 클립보드에 복사
        emoji[e][e] = nt
        q.append((e, e, nt))
    
    ne = e + c
    if c > 0 and 0 < ne <= s  and (emoji[ne][c] > nt or emoji[ne][c] == 0): # 클립보드 붙여넣기
        emoji[ne][c] = nt
        q.append((ne, c, nt))
    
    ne = e - 1
    if e - 1 > 1 and (emoji[ne][c] > nt or emoji[ne][c] == 0): # 이모티콘 1개 삭제
        emoji[ne][c] = nt
        q.append((ne, c, nt)) 
    
print(result)