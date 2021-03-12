# 연구소
# tuble이 list보다 속도가 빠름

from collections import deque
from itertools import combinations
# import copy
import sys
input = sys.stdin.readline

def bfs(lab) : # 바이러스 퍼트리기
    q = deque(virus)
    while q :
        x, y = q.popleft()
        for i, j in d :
            nx, ny = x + i, y + j
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0 :
                lab[nx][ny] = 2
                q.append((nx, ny))
    cnt = 0 
    for i in lab : # 안전 영역 세기
        cnt += i.count(0)
    return cnt

# def dfs(L) : # 벽 세우기
#     global result
#     if L == 3:
#         lab = [i[:] for i in metrix]
#         result = max(result, bfs(lab))
#         return
#     for i, j in empty :
#         if metrix[i][j] == 0 :
#             metrix[i][j] = 1
#             dfs(L + 1)
#             metrix[i][j] = 0


if __name__=="__main__" :
    n, m = map(int, input().split())
    metrix = [] # 전체 공간
    empty = [] # 비어있는 칸
    virus = [] # 바이러스
    d = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    result = 0 # 안전 영역 크기 최댓값

    for i in range(n) :
        metrix.append(list(map(int, input().split())))
        for j in range(m) :
            if metrix[i][j] == 2 :
                virus.append((i, j))
            if metrix[i][j] == 0 :
                empty.append((i, j))
    
    for case in list(combinations(empty, 3)): # 함수 호출하는 형태는 시간이 많이 걸리므로 combinations 이용
        # lab = copy.deepcopy(metrix) # 기존의 연구실 상태 유지를 위해 깊은 복사
        lab = [i[:] for i in metrix] # deepcopy는 시간이 많이 소요되므로 slicing을 이용하는 것이 좋음
        for i, j in case :
            lab[i][j] = 1
        result = max(result, bfs(lab))

    # dfs(0)

    print(result)

'''
combinations가 훨씬 빠른 이유?
1. tuple을 이용한 형태 (tuple이 속도가 더 빠름)
2. 함수 호출이 아닌 반복문 사용 (while문을 이용한 형태)
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n: # 조합이 생성될 수 없는 경우
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices) # 처음으로 만들 수 있는 조합 반환
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else: # 조합을 모두 찾았으므로 종료
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices) # while문이 종료될 때까지 생성된 조합 반환
'''