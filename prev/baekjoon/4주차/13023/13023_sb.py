# ABCDE
# A-B-C-D-E와 같은 형태로 친구 관계가 이루어지는지 확인하는 문제
# 0-1-2-3-0 처럼 같은 수로 돌아가도 4번의 관계가 연결되어 있으면 위와 같은 친구 관계 성립!

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [0] * n # 지나온 경로 표시
relation = [[] for _ in range(n)] # 친구 관계 리스트

for _ in range(m) : # 관계에 대해 인덱스를 기준으로 정리
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

def dfs(num, cnt) :
    if cnt == 4 : # 관계가 4번 연결되면 원하는 조건 만족
        print(1)
        exit()
    for i in relation[num] :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(i, cnt + 1)
            visited[i] = 0
    

for i in range(n) : # 사람별로 확인
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0
print(0) # 프로그램이 for문이 끝날 때까지 종료되지 않으면 조건을 만족하는 친구 관계가 없으므로 0 출력