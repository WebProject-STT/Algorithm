# 숨바꼼질3
import sys
from collections import deque

def BFS(N, K):
    queue = deque()
    queue.append(N) # 위치, 시간

    while queue:
        X = queue.popleft()
        if X == K:
            return visited[X]
        
        # 수빈이가 이동할 수 있는 방법은 3가지
        for next_x in (X-1, X+1, X*2):
            if 0 <= next_x < 100001 and not visited[next_x]:
                if next_x == X*2 and X != 0:
                    visited[next_x] = visited[X]
                    queue.appendleft(next_x)
                else:
                    visited[next_x] = visited[X] + 1
                    queue.append(next_x)
        # if X*2 < 100001:
        #     if not visited[X*2] and X != 0:
        #         queue.appendleft(X*2) # X*2가 더 높은 순위를 가져야 빠르게 출력해서 나갈 수 있기 때뮨이다
        #         visited[X*2] = visited[X]
        # if X+1 < 100001:
        #     if not visited[X+1]:
        #         queue.append(X+1)
        #         visited[X+1] = visited[X]+1
        # if 0 <= X-1:
        #     if not visited[X-1]:
        #         queue.append(X-1)
        #         visited[X-1] = visited[X]+1
                        
N, K = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(BFS(N, K))


"""
# 메모리 초과 사용 x
# 숨바꼼질3
import sys
from collections import deque

def BFS(N, K):
    global min_
    visited = [False for i in range(100001)]
    queue = deque()
    queue.append((N, 0)) # 위치, 시간

    while queue:
        X, time = queue.popleft()
        if X == K:
            min_ = min(min_, time)
            continue
        
        # 수빈이가 이동할 수 있는 방법은 3가지
        if X*2 < 100001:
            if not visited[X*2] and X*2 != 0 and time < min_:
                queue.append((X*2))
        if X+1 < 100001:
            if not visited[X+1] and time+1 < min_:
                queue.append((X+1, time+1))
        if 0 <= X-1:
            if not visited[X-1] and time+1 < min_:
                queue.append((X-1, time+1))
    return min_
                        
N, K = map(int, sys.stdin.readline().split())
min_ = sys.maxsize
print(BFS(N, K))

"""
