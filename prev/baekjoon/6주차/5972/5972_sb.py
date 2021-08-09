# 택배 배송
import heapq # 다익스트라 알고리즘을 사용하기 위해 최소 힙 필요
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
route = [[] for _ in range(n + 1)]

def dijkstra() : # 다익스트라 알고리즘을 통해 최단 경로를 찾는 함수
    distances = [float('inf')] * (n+1) # 거리 저장을 위한 리스트 (거리를 무한대로 초기화)
    distances[1] = 0 # 시작 정점의 거리를 0으로 초기화
    q = [] # 모든 정점이 저장될 큐 생성
    heapq.heappush(q, (0, 1)) # 시작 정점의 거리와 시작 정점을 최소 힙에 넣어줌
    while q :
        cur_distance, cur_vertex = heapq.heappop(q) # 현재 정점 거리와 정점을 큐에서 꺼냄
        if distances[cur_vertex] < cur_distance : # 더 짧은 경로가 있다면 무시
            continue
        for next_v, weight in route[cur_vertex] : # 가중치를 모두 확인
            d = cur_distance + weight
            if d < distances[next_v] : # 현재 정점이 더 가까우면 거리 업데이트
                distances[next_v] = d
                heapq.heappush(q, (d, next_v))
    return distances[-1]

for _ in range(m) :
    i, j, w = map(int, input().split())
    route[i].append((j, w))
    route[j].append((i, w))

print(dijkstra())