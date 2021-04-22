# 치킨배달
import sys

def distance(chicken) : # 거리를 계산하는 함수
    dist = 0
    for r1, c1 in home :
        dist += min([(abs(r1-r2) + abs(c1-c2)) for r2, c2 in chicken])
    return dist

def dfs(L, cur) : # 조합을 만들어 치킨 거리의 최솟값을 찾는 함수
    global min_dist
    if L == M :
        select_chicken = [chicken[i] for i in range(chilen) if visited[i]]
        min_dist = min(min_dist, distance(select_chicken))
        return
    
    for i in range(cur, chilen) :
        if visited[i] == 0 :
            visited[i] = 1
            dfs(L + 1, i + 1)
            visited[i] = 0

if __name__=="__main__" : 
    input = sys.stdin.readline

    N, M = map(int, input().split()) # 도시 크기, 치킨집 개수
    city = [] # 도시
    chicken = [] # 치킨집
    home = [] # 집

    for r in range(N) :
        temp = list(map(int, input().split()))
        city.append(temp) # 도시의 각 행에 대한 정보 추가
        for c in range(N) :
            if temp[c] == 2 :# 치킨집인 경우
                chicken.append((r,c))
            elif temp[c] == 1 : # 집인 경우
                home.append((r,c))
    
    if len(chicken) == M : # 이미 M개이므로 치킨집을 폐업시킬 필요가 없음
        print(distance(chicken))
    else : # M개씩 조합을 만들어 도시의 치킨 거리의 최솟값을 찾아야 함
        min_dist = 2147000000 # 대략적인 큰 수로 도시의 치킨 거리 초기화
        chilen = len(chicken)
        visited = [0] * chilen
        dfs(0, 0)
        print(min_dist)



'''
NxN 크기의 도시는 빈 칸(0), 집(1), 치킨집(2) 중 하나로 구성되어 있다.
치킨 거리는 집과 가장 가까운 치킨집 사아의 거리이며,
도시의 치킨 거리는 모든 집의 치킨 거리 합이다.
거리 d = |r1-r2| + |c1-c2| 이다.
도시에 있는 치킨집 중 최대 M개를 고르고 나머지 치킨집은 모두 폐업시킬 때,
도시의 치킨 거리의 최솟값을 출력한다.
---
치킨집을 M개로 조합을 만들고
각 조합에 대한 도시의 치킨 거리를 구하며 최솟값을 업데이트한다.
'''