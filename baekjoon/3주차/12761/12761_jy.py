# 돌다리
A, B, N, M = map(int, input().split())
from collections import deque

m = [1, -1, +A, +B, -A, -B, A, B]
queue = deque([])
visited = [0 for _ in range(100001)]

def bfs():
    while queue:
        node, count = queue.popleft()
        temp = [node+1, node-1, node+A, node-A, node+B, node-B, node*A, node*B]
        check = True
        for next_ in temp:
            if 0 <= next_ <= 100000 and visited[next_] == 0:
                if next_==M:
                    check = False
                else:
                    visited[next_] = 1
                    queue.append((next_, count+1))
        if not check:
            print(count+1)
            break
            
queue.append((N, 0))
visited[N] = 1
bfs()

# 두 개 다 시간 비슷

"""
# 돌다리
A, B, N, M = map(int, input().split())
from collections import deque

m = [1, -1, +A, +B, -A, -B, A, B]
queue = deque([])
visited = [0 for _ in range(100001)]
min_ = abs(N-M) + 1

def bfs():
    global min_
    while queue:
        node, count = queue.popleft()
        temp = [node+1, node-1, node+A, node-A, node+B, node-B, node*A, node*B]
        check = True
        for next_ in temp:
            if 0 <= next_ <= 100000 and visited[next_] == 0:
                if next_==M:
                    min_ = min(min_, count+1)
                else:
                    visited[next_] = 1
                    queue.append((next_, count+1))
            
queue.append((N, 0))
visited[N] = 1
bfs()
print(min_)
"""