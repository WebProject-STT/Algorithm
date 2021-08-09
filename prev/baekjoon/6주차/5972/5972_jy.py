# 택배 배송
import sys
import heapq
INF = sys.maxsize
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1) # 거리 배열 -> INF로 초기화 해주기

def dijkstra(start):
    queue = [] # 우선순위 큐 선언
    heapq.heappush(queue, (0, start)) # 우선순위 큐에 추발점 값을 넣어준다.
    dis[start] = 0 # 출발점은 거리 = 0 즉 1번 노드의 값은 0
    while queue: # queue에 노드 없으면 끝!
        d, now = heapq.heappop(queue) # 탐색할 노드, 거리 가져오기
        if dis[now] < d: continue # 기존에 있는 거리보다 길면 패스!
        for v, w in graph[now]:
            cost = d + w # 해당 노드에서 거쳐갈 거리
            if cost < dis[v]: # 알고 있는 거리보다 작으면 갱신
                dis[v] = cost
                heapq.heappush(queue, (cost, v))
    return dis


for _ in range(M):
    n1, n2, w = map(int, sys.stdin.readline().split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))

print(dijkstra(1))