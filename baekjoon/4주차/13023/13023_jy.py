# ABCDE
import sys
from collections import defaultdict
num_s, num_r= map(int,sys.stdin.readline().split())

relations = defaultdict(list)
for _ in range(num_r):
    r1, r2 = map(int,sys.stdin.readline().split())
    relations[r1].append(r2)
    relations[r2].append(r1)
answer = False

def DFS(cur_idx, count):
    global answer
    if count >= 4:
        answer = True
        return
    visited[cur_idx] = 1
    # cur_id가 갈수 있는 모든 경로
    for next_ in relations[cur_idx]:
        if not visited[next_]:
            DFS(next_, count+1)
            visited[next_] = 0
        if answer: return
  
visited = [0]*num_s
for i in range(num_s):
    DFS(i, 0)
    visited[i] = 0
    if answer:
        print(1)
        break
else: print(0)