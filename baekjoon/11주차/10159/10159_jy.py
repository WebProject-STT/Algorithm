# 저울
def dfs(start, li, visited):
    visited[start] = 1
    for node in li[start]:
        if not visited[node]:
            dfs(node, li, visited)
    
    return visited

if __name__ == "__main__":
    N = int(input()) + 1
    M = int(input())
    parent, child = [[] for _ in range(N)], [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        parent[a].append(b)
        child[b].append(a)
    
    for i in range(1, N):
        temp = N - 1
        visited = dfs(i, parent, [0]*N)
        visited = dfs(i, child, visited)
        temp -= sum(visited)
        print(temp)

"""
[1]>[2], [2]>[3], [3]>[4], [5]>[4], [6]>[5]
[2]>[3], [3]>[4] => [2] > [4]
2는 1, 3, 4와 비교 결과를 알 수 있지만 5, 6과의 비교 결과 알 수 X
4는 모든 물건과 비교 결과 알 수있음
"""