# 아기 상어
import sys
from collections import deque
dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)]
N = int(sys.stdin.readline())
grids = [] # 전체 격자 
fish_nums = 0 # 물고기 수
shark_r, shark_c = 0, 0 # 아기상어 위치
shark_w = 2 # 아기상어 무게

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    grids.append(temp)
    for j in range(N):
        if temp[j] == 9:
            shark_r, shark_c = i, j
            grids[i][j] = 0
            continue
        if temp[j]:
            fish_nums += 1
            continue

# 근처 물고기들 중 가장 가까운 물고기 찾기
def find_min_fish(cur_r, cur_c, shark_w):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[cur_r][cur_c] = 1
    queue = deque()
    queue.append((cur_r, cur_c, 0)) # 현재 위치, 거리
    can_eat = []
    min_ = sys.maxsize
    while queue:
        r, c, distance = queue.popleft()
        if distance > min_: break

        for i in range(4):
            next_r, next_c = r+dir_[i][0], c+dir_[i][1]
            if 0 <= next_r < N and 0 <= next_c < N: # 아기 상어 갈 수 있는 곳
                if not visited[next_r][next_c] and grids[next_r][next_c] <= shark_w: # 아기 상어가 지나갈 수 있는 곳이면 
                    visited[next_r][next_c] = 1
                    queue.append((next_r, next_c, distance+1))
                if  0 < grids[next_r][next_c] < shark_w and min_ >= distance+1: # 아기 상어가 먹을 수 있는 물고기이면
                    min_ = distance+1
                    can_eat.append((next_r, next_c, distance+1))
                
    print("can_eat 1 ; ",can_eat)
    can_eat = sorted(set(can_eat), key=lambda x: (x[0], x[1])) # -인 이유 -> 가장 위쪽 -> 가장 왼쪽
    print("can_eat 2 ; ",can_eat)
    if can_eat:
        return can_eat[0][0], can_eat[0][1], can_eat[0][2]
    else: return False


if __name__ == "__main__":

    count_weight = 0
    total_dis = 0
    while fish_nums:
        result = find_min_fish(shark_r, shark_c, shark_w)
        if result: # 먹을게 있다면
            #print("result : ", result)
            shark_r, shark_c= result[0], result[1] # 마지막 아기상어 위치 update
            total_dis += result[2] # 거리=> 이동 시간의미하므로 update
            fish_nums -= 1 # 물고기 한마리 냠 했으니 물고기 수 줄어듬
            grids[shark_r][shark_c] = 0 # 먹었으니까 0으로 업뎃
            count_weight += 1 
            if count_weight == shark_w: # 아기상어 무게 만큼 물고기 냠 하면 weight+1이고 count_weight는 0 세팅
                shark_w += 1
                count_weight = 0
        else: # 먹을게 없으면 엄마상어한테 이르러감
            print(total_dis)
            break
    if not fish_nums: print(total_dis)

