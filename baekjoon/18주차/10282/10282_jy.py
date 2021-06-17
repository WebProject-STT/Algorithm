# 해킹
import sys
from collections import defaultdict
import heapq

INF = sys.maxsize

# dfs = 런타임 에러(Recursion 에러)
def virus(cur_virus):
    global visitied
    if cur_virus not in relation.keys(): return

    for idx, next_virus in enumerate(relation[cur_virus][0]):
        if visitied[next_virus] == -1 or (visitied[next_virus] > relation[cur_virus][1][idx]):
            visitied[next_virus] = relation[cur_virus][1][idx]
            virus(next_virus)
    return

def dijkstra(start):
    queue = []# 우선 순위 큐 => 사용 이유? heapq는 sort되어 있기 때문에 cost 비용이 가장 작은 값을 먼저 꺼낼 수 있다/\.
    heapq.heappush(queue, (0, start)) # 우선순위 큐에 출발점 값 넣어줌(비용, 노드)
    dis = [INF]*(n+1) # 거리 배열 (INF로 초기화)
    dis[start] = 0 # 출발점은 거리 0(여기서 시작하는 거니까 따로 거리 없음)

    while queue: # queue에 노드 없으면 끝임.
        d, now = heapq.heappop(queue) # 탐색할 노드, 거리 가져오기
        if dis[now] < d: continue # 기존에 있는 거리보다 길면 패스!
        for v, w in relation[now]: # 현재 노드랑 이어져 있는(의존성 있는) 노드, 값
            cost = d + w # 해당 노드에서 거쳐갈 거리(현재 노드+다음 노드 거리)
            if cost < dis[v]: # 다음 갈 노드의 거리가 현재에서 가는 것 보다 크면 change
                dis[v] = cost
                heapq.heappush(queue, (cost, v))
    
    count, time = 0, 0
    for d in dis:
        if d != INF:
            count +=1
            time = max(time, d)
    return count, time

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, d, c = map(int, input().split())

        relation = defaultdict(list)
        visitied = [-1]*(n+1)
        visitied[c] = 0
        for _ in range(d):
            a, b, s = map(int, input().split())
            relation[b].append([a, s])
            
            # if b not in relation.keys():
            #     relation[b] = [[a], [s]]
            # else:
            #     relation[b][0].append(a)
            #     relation[b][1].append(s)

        result = dijkstra(c)
        print(result[0], result[1])
