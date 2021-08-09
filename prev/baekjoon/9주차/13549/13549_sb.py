# 숨바꼭질 3
from collections import deque

def solution(N, K) :
    limit = 100001 # 최대로 주어지는 점 + 1
    time = [-1] * limit # 시간 저장을 위한 리스트 (방문 여부 확인을 위해 -1로 초기화)
    time[N] = 0 # 시작은 0초
    d = [2, -1, 1]

    q = deque()
    q.append(N)

    while q :
        X = q.popleft()
        if X == K :
            return time[X]
        for i in range(3) :
            if i == 0 : # 수빈이가 순간이동하는 경우
                nx = X * d[i]
                if 0 < nx < limit and time[nx] == -1:
                    time[nx] = time[X]
                    q.appendleft(nx)
            else : # 수빈이가 걷는 경우
                nx = X + d[i]
                if 0 <= nx < limit and time[nx] == -1 :
                    time[nx] = time[X] + 1
                    q.append(nx)

if __name__=="__main__" :
    N, K = map(int, input().split()) # 수빈이 위치, 동생 위치
    print(solution(N, K))
'''
수빈이가 걷는다면 1초 후 X-1 또는 X+1 위치로 이동
수빈이가 순간이동 하면 0초 후 X*2의 위치로 이동
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초인지 구하기
--- 풀이 (돌다리 유사 문제)
수빈이와 동생이 존재할 수 있는 점의 위치는 100000이므로 그것에 1을 더해 limit로 지정한다.
수빈이의 이동 시간을 저장할 time 리스트를 만든다.
이 때, 방문하지 않은 X점에 대한 시간이 기록되어 있지 않으므로 이것을 기준으로 점의 방문 여부도 판별한다.
동생의 위치로 가기 위해 계산을 할 때 순간이동이 가장 가까이 다가갈 수 있으므로 우선순위가 높아야한다.
그러므로 deque의 맨 처음 위치로 넣어주며 진행할 수 있도록 조정한다.
'''