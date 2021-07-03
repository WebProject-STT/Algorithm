# 운동
import sys
INF = sys.maxsize

if __name__ == "__main__":
    V, E = map(int, input().split())

    dp = [[INF for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        dp[a][b] = c # a(출발) , b(도착), c (거리)
    
    for k in range(1, V+1): # 경유
        for start in range(1, V+1): # 출발
            for end in range(1, V+1): # 도착
                dp[start][end] = min(dp[start][end], dp[start][k]+dp[k][end])
    
    # 가장 작은 사이클을 찾아라
    min_ = INF
    for i in range(1, V+1):
        min_ = min(min_, dp[i][i]) # 출발-나, 도착-나 인 경로 중 가장 작은 것
    
    if min_ == INF: print(-1)
    else: print(min_)
"""
def dfs(start, current, visit, length):
    global min_, visited
    if length > min_: return
    if length != 0 and start == current:
        min_ = min(min_, length)
        visited = visit[:]
        return

    for idx, next_ in enumerate(edges[current][0]):
        if not visit[next_]:
            visit[next_] = 1
            dfs(start, next_, visit, length+edges[current][1][idx])
            visit[next_] = 0
    return

if __name__ == "__main__":
    V, E = map(int, input().split())

    edges = dict()
    for _ in range(E):
        a, b, c = map(int, input().split())
        if a not in edges.keys():
            edges[a] = [[b], [c]]
        else:
            edges[a][0].append(b)
            edges[a][1].append(c)

    visited = [0]*(V+1)
    for start in range(1, V+1):
        dfs(start, start, visited, 0)
    print(min_)

"""