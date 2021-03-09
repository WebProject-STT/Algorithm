# 촌수 계산
import sys
from collections import defaultdict
nums = int(sys.stdin.readline())
start, end = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
relations = defaultdict(list)
visited = [0]*nums
for _ in range(n):
    p, c = map(int,sys.stdin.readline().split())
    p -= 1
    c -= 1
    relations[p].append(c)
    relations[c].append(p)

stack = [start-1]
while stack:
    n = stack.pop()
    for node in relations[n]:
        if not visited[node]:
            visited[node] = visited[n] + 1
            stack.append(node)
if not visited[end-1]: print(-1)
else: print(visited[end-1])