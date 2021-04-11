# 게리맨더링
import sys
from collections import deque, defaultdict
N = int(sys.stdin.readline())
peoples = [0]+list(map(int, sys.stdin.readline().split()))
cities = defaultdict(list)
count = 0
for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    cities[i] = temp[1:]
    if not temp[1:]:
        count += 1

min_ = sys.maxsize

def dfs(check_combi):
    if len(check_combi) == 1: return True
    d_visited = [False]*(N+1)
    d_visited[check_combi[0]]=True
    stack = [check_combi[0]]
    while stack:
        for n in cities[stack.pop()]:
            if not d_visited[n] and n in check_combi:
                d_visited[n] = True
                stack.append(n)
    
    for i in range(1, N):
        if i in check_combi and not d_visited[i]: return False
    return True

def check_connect(combi1, combi2):
    global min_

    if dfs(combi1) and dfs(combi2):
        diff = abs(sum([peoples[idx] for idx in combi1]) - sum([peoples[idx] for idx in combi2]))
        min_ = min(min_, diff)
    
    return

def find_combi(cur_num, last_num, combi_num):
    if cur_num == combi_num:
        combi1, combi2 = [], []
        for i in range(1, N+1):
            if visited[i]: combi1.append(i)
            else: combi2.append(i)
        check_connect(combi1, combi2)
        return
    
    for i in range(last_num+1, N+1):
        if not visited[i]:
            visited[i] = True
            find_combi(cur_num+1, i, combi_num)
            visited[i] = False

if count != N:
    M = N//2
    for i in range(1, M+1): # 반만 조합 구하면 반대편 구해짐
        if i == 1:
            for i in range(1, N+1):
                temp = [j for j in range(1, N+1) if j != i]
                check_connect([i], temp)
        else:
            visited = [False]*(N+1)
            for j in range(1, N+1):
                visited[j] = True
                find_combi(1, j, i)
                visited[j] = False

if min_ == sys.maxsize:
    print(-1)
else:
    print(min_)
