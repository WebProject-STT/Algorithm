# 스티커
import sys
num = int(sys.stdin.readline())

for _ in range(num):
    num2 = int(sys.stdin.readline())
    case = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    visited = [[0 for _ in range(len(case[0]))] for _ in range(2)]
    
    visited[0][0] = case[0][0]
    visited[1][0] = case[1][0]
    visited[0][1] = visited[1][0] + case[0][1]
    visited[1][1] = visited[0][0] + case[1][1]

    for i in range(2, num2):
        visited[0][i] = max(visited[1][i-1] + case[0][i], visited[1][i-2] + case[0][i])
        visited[1][i] = max(visited[0][i-1] + case[1][i], visited[0][i-2] + case[1][i])
    print(max(visited[0][-1], visited[1][-1]))

"""
for _ in range(num):
    num2 = int(sys.stdin.readline())
    case1, case2, visited= [],[],[0 for _ in range(num2*2)]
    dir_ = [-num2, num2, -1, 1]# 북 남 서 동
    max_ = 2*num2
    for i in range(2):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(len(temp)):
            case1.append(temp[j])
            case2.append((num2*i+j, temp[j])) # (i, j) 위치 / temp[j] 값
    case2 = sorted(case2, key=lambda x: -x[1]) # 값에 대해 sort
    
    total = 0
    for value in case2:
        if visited[value[0]]: continue
        total += value[1]
        for i in range(4):
            next_ = value[0]+dir_[i]
            if 0 <= next_ < max_: # 범위안에 있으면
                visited[next_] = 1
    print(total)
"""