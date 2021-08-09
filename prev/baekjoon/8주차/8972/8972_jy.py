# 미친 아두이노
import sys
from collections import defaultdict
R, C = map(int, sys.stdin.readline().split())
cur_r, cur_c = 0, 0
crazy_robots = []
dir_ = [(0, 0), (1, -1), (1, 0), (1, 1),
        (0, -1), (0, 0), (0, 1),
        (-1, -1), (-1, 0), (-1, 1)]

for i in range(R):
    temp = sys.stdin.readline()
    for j in range(C):
        if temp[j] == 'I':
            cur_r, cur_c = i, j
            continue
        if temp[j] == 'R':
            crazy_robots.append([i, j])
            continue
crazy_robots_num = len(crazy_robots)
directions = [dir_[int(s)] for s in sys.stdin.readline()[:-1]]

for i in range(len(directions)):
    # 1. 종수의 다음 아두이노 위치
    cur_r, cur_c = cur_r+directions[i][0], cur_c+directions[i][1]
    # 2. 종수 아두이노=미친 아두이노 겜 끝
    if [cur_r, cur_c] in crazy_robots:
        print(f"kraj {i + 1}")
        sys.exit(0)
    # 3 ~ 5.
    new_robots = defaultdict(list)
    for r_i in range(crazy_robots_num):
        robot_r, robot_c = crazy_robots[r_i][0], crazy_robots[r_i][1]
        min_, min_r, min_c = sys.maxsize, robot_r, robot_c # 만약 다 움직이지 못하면 가만히 있기
        # 3. 미친 아두이노의 다음 위치 찾기
        for idx in range(1, 10):
            if idx == 5: continue
            next_robot_r, next_robot_c = robot_r+dir_[idx][0], robot_c+dir_[idx][1]
            if 0 <= next_robot_r < R and 0 <= next_robot_c < C:
                dis = abs(cur_r - next_robot_r) + abs(cur_c - next_robot_c)
                if min_ > dis: # 가장 거리가 짧은 것 저장
                    min_, min_r, min_c = dis, next_robot_r, next_robot_c
        # 4. 종수 아두이노=미친 아두이노 겜 끝
        if cur_r == min_r and cur_c == min_c:
            print(f"kraj {i + 1}")
            sys.exit(0)
        new_robots[str(min_r)+' '+str(min_c)].append(r_i)

    del crazy_robots
    # boom이 일어난거 아두이노 제거
    crazy_robots = []
    for key, value in new_robots.items():
        if len(value) == 1:
            crazy_robots.append(list(map(int, key.split())))
    crazy_robots_num = len(crazy_robots)
else:
    grids = [['.']*C for _ in range(R)]
    for r, c in crazy_robots:
        grids[r][c] = 'R'
    grids[cur_r][cur_c] = 'I'
    for line in grids:
        print(''.join(line))