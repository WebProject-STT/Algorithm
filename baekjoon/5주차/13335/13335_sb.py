# 트럭
from collections import deque
import sys
input = sys.stdin.readline

n, w, l = map(int, input().split()) # 트럭 수, 다리 길이, 다리 최대 하중
a = list(map(int, input().split())) # 트럭 무게 (최대 10)

q = deque([0]*(w-1))
q.append(a[0])
time, idx, qsum = 1, 1, a[0] # 다리 건너는 시간, a의 인덱스 위치, 현재 다리에 있는 트럭 총 무게


while True :
    if qsum == 0 : # 모든 트럭이 다리를 지나감
        break
    qsum -= q.popleft()
    if idx < n and qsum + a[idx] <= l : # 트럭을 추가할 수 있는지 확인
        q.append(a[idx])
        qsum += a[idx]
        idx += 1
    else :
        q.append(0)
    time += 1 # 시간은 1초식 흐름

print(time)