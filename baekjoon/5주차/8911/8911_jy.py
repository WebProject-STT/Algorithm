# 거북이
import sys
num = int(sys.stdin.readline())
cases = [sys.stdin.readline()[:-1] for _ in range(num)]

# 기본 setting -> 방향들
# 1. 기본 dir = F 갈 곳
F_dir = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동 서 남 북
# 2. B 갈 곳
"""
동 -> B(서)
서 -> B(동)
남 -> B(북)
북 -> B(남)
"""
B_dir = (1, 0, 3, 2) 
# 3. L로 인한 방향 변경 & R로 인한 방향 변경
# 동(0) -> 북(3), 서(1) -> 남(2), 남(2) -> 동(0), 북(3) -> 서(1)
change_dir_L = (3, 2, 0, 1)
# 동(0) -> 남(2), 서(1) -> 북(3), 남(2) -> 서(1), 북(3) -> 동(0)
change_dir_R = (2, 3, 1, 0)


for case in cases:
    len_ = len(case)
    visited = [(0, 0)]
    cur_r, cur_c, cur_dir = 0, 0, 3 # 초기 방향 북(3)
    max_r, max_c = 0, 0
    min_r, min_c = 0, 0
    for d in case:
        print("check : ",d, cur_dir, (cur_r, cur_c))
        if d=='F' or d == 'B':
            if d=='F':
                cur_r += F_dir[cur_dir][0]
                cur_c += F_dir[cur_dir][1]
            else:
                cur_r += F_dir[B_dir[cur_dir]][0]
                cur_c += F_dir[B_dir[cur_dir]][1]
            if (cur_r, cur_c) not in visited: # 들린 적 없으면 추가
                visited.append((cur_r, cur_c))
                max_r = max(max_r, cur_r) # 현재 row위치와 양의 방향 row축 최대 길이 비교
                min_r = min(min_r, cur_r)
                max_c = max(max_c, cur_c) # 현재 col위치와 양의 방향 col축 최대 길이 비교
                min_c = min(min_c, cur_c)
            continue
        # 방향 변경
        if d == 'L':
            cur_dir = change_dir_L[cur_dir]
            continue
        if d == 'R':
            cur_dir = change_dir_R[cur_dir]
            continue    
    print(abs(max_r - min_r)*abs(max_c - min_c))