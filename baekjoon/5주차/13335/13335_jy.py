# 트럭
import sys
from collections import deque
num, W, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

queue = deque()
idx, times, len_ = 0, 1, len(trucks)
queue.append((idx, times)) # queue에 첫번째 인덱스, 두번째는 시간
weight = trucks[0] # 현재 weight 값을 저장
while queue: # queue가 차 있고, idx < len일때 까지 진행
    times += 1 # 시간 증가
    #print("q1 : ", idx, weight, queue, times)
    if queue[0][1] + W == times: # truck 빼기(들어온 시간 + W 이면)
        i_, w_ = queue.popleft()
        weight -= trucks[i_] # 뺀 truck의 중량은 제거
    if idx+1 < len_ and weight+trucks[idx+1] <= L: # truck 넣을 수 있음 넣기
        idx += 1
        queue.append((idx, times))
        weight += trucks[idx] # 추가한 truck의 중량
    #print("q2 : ", idx, weight, queue)
print(times)