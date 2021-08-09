# 촌수계산

import sys
input = sys.stdin.readline

n = int(input()) # 전체 사람 수
x, y = map(int, input().split()) # 촌수를 계산해야하는 두 사람
m = int(input()) # 관계 수
relation = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m) : # 관계에 대해 인덱스를 기준으로 정리
    i, j = map(int, input().split())
    relation[i].append(j)
    relation[j].append(i)

cnt = 0 # 관계 수
def dfs(num) :
    global cnt
    if num == y : # 원하는 사람과의 관계를 찾으면
        print(cnt) # 관계 수를 출력하고
        exit() # 종료
    if visited[num] == 0 :
        visited[num] = 1
        for i in range(len(relation[num])) :
            cnt += 1
            dfs(relation[num][i])
            cnt -= 1
    else :
        return

dfs(x)
print(-1) # 관계 수를 출력하지 못한 경우 종료되지 않았으므로 -1 출력