# 게리멘더링
import sys
from collections import deque

# 구역이 모두 연결되어 있는지 확인하는 함수
# arr : 선거구의 구역 정보를 담은 리스트
def check(arr) :
    q = deque()
    visited = [0] * (n+1)
    q.append(arr[0])
    cnt, sum_ = 1, 0 # cnt : 길이 확인용, sum_ : 합산용
    visited[arr[0]] = 1
    while q :
        i = q.popleft()
        sum_ += people[i]
        for j in relation[i] :
            if visited[j] == 0 and j in arr :
                visited[j] = 1
                cnt += 1
                q.append(j)
    if cnt == len(arr) :
        return sum_
    else :
        return 0


# 두 선거구로 만드는 함수 
# key : 원하는 길이, L : 현재 길이, cur : 현재 index
def combi(key, L, cur):
    global min_
    if L == key :
        # 두 선거구로 만들기
        zone1, zone2 = [], []
        for i in range(1, n+1) :
            if combi_visited[i] : zone1.append(i)
            else : zone2.append(i)
        # 두 구역의 연결에 대한 확인
        z1 = check(zone1)
        z2 = check(zone2)
        # 두 구역 모두 연결되어 있는 경우 차와 최솟값 구하기
        if z1 and z2 : 
            dif = abs(z1 - z2)
            min_ = min(min_, dif)
        return
    for i in range(cur, n+1) :
        if combi_visited[i] == 0:
            combi_visited[i] = 1
            combi(key, L+1, cur+1)
            combi_visited[i] = 0
        

if __name__=="__main__" :
    input = sys.stdin.readline

    n = int(input())
    people = [0] + list(map(int, input().split()))
    relation = [[0]]
    for _ in range(n) : # 구역 간의 관계
        temp = list(map(int, input().split()))
        relation.append(temp[1:])
    
    min_ = sys.maxsize # 최솟값을 가장 큰 값으로 초기화

    # 두 선거구 만들기 (조합)
    for i in range(1, n//2 + 1) : # 반만 구하면 됨
        combi_visited = [0] * (n+1)
        combi(i, 0, 1)
    
    if min_ == sys.maxsize :
        print(-1)
    else :
        print(min_)
        


'''
두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값 출력
두 선거구로 나눌 수 없는 경우에는 -1 출력
---
두 선거구로 나누기 => 조합
각 선거구의 구역들이 모두 연결되어 있는지 확인 => bfs
만약 연결되어 있다면 두 선거구의 인구 차이 구하기
---
비트마스킹과 멱집합을 이용한 방식
https://m.blog.naver.com/kmh03214/221682736440
'''