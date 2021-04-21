# 치킨배달 (https://www.acmicpc.net/problem/15686)
import sys
from collections import deque

def distance(temp_chickens):
    total = 0
    for h in house:
        min_t = 2*N-2
        for t in temp_chickens:
            temp = abs(h[0]-t[0]) + abs(h[1]-t[1])
            if temp < min_t: min_t = temp
        total += min_t
    return total

def dfs(cur_num, last_num):
    global min_
    if cur_num == M-1:
        temp_chicken = []
        for i in range(len_c):
            if visited[i]: 
                r, c = chickens[i]//N, chickens[i]%N
                temp_chicken.append((r, c))
        min_ = min(distance(temp_chicken), min_)
        return
    
    for i in range(last_num+1, len_c):
        if not visited[i]:
            visited[i] = True
            dfs(cur_num+1, i)
            visited[i] = False

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    grids = []
    chickens = []
    house = []
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(len(temp)):
            if temp[j] == 0: continue
            elif temp[j] == 2: chickens.append(N*i+j)
            else: house.append((i, j))
        del temp
    
    len_c = len(chickens)

    if len_c == M: # 바로 거리 구하기
        temp_chicken1 = []
        for num in chickens:
            temp_chicken1.append((num//N, num%N))
        min_ = distance(temp_chicken1)
    else:# 조합 구하기
        min_ = 32500
        visited = [False]*len_c
        for i in range(len_c):
            visited[i] = True
            dfs(0, i)
            visited[i] = False
            
    print(min_)

            