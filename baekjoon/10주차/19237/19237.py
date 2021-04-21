# 어른 상어 (https://www.acmicpc.net/problem/19237)
import sys
from collections import defaultdict
dirs = [(0), (-1, 0), (1, 0), (0, -1), (0, 1)] # [위, 아래, 왼쪽, 오른쪽]

def shark_start():
    global sharks_pos, sharks_cur_dir
    for time in range(1, 1001):
        # 1. 현재 위치에서 이동 -> 다음 이동할 위치
        boom_check = dict() # 해당 위치에 boom 일어 났는지 check
        new_shark = []
        for idx, r, c in sharks_pos:
            cur_dir = sharks_cur_dir[idx]
            # 1-1. 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
            for d in sharks_dirs[idx][cur_dir-1] :# 샤크 번호의 현재 바라보고 있는 방향의 우선순위
                nr, nc = r+dirs[d][0], c+dirs[d][1]
                if 0 <= nr < N and 0 <= nc < N and not grids[nr][nc][0]: # grids[nr][nc][0] = 냄새가 없다
                    temp = str(nr)+' '+str(nc)
                    if temp not in boom_check.keys(): boom_check[temp] = (idx, d)
                    else:
                        if boom_check[temp][0] > idx: boom_check[temp] = (idx, d)
                    break
            else: # 인접칸 다 돌았는데 갈 곳이 없다
                # 1-2. 자신의 냄새가 있는 칸의 방향으로 잡는다
                for d in sharks_dirs[idx][cur_dir-1] :
                    nr, nc = r+dirs[d][0], c+dirs[d][1]
                    if 0 <= nr < N and 0 <= nc < N and grids[nr][nc][0] == idx: # grids[nr][nc][0] = 자신의 냄새가 있는 칸
                        boom_check[str(nr)+' '+str(nc)] = (idx, d)
                        break
                else: # 그런데도 없으면 그냥 원래 정보 저장
                    boom_check[str(r)+' '+str(c)] = (idx, cur_dir)
        del sharks_pos
        sharks_pos = []
        for key, value in boom_check.items():
            r, c = map(int, key.split())
            grids[r][c] = (value[0], k+1) # k+1하는 이유 밑에서 바로 냄새빼기 하니까
            sharks_pos.append((value[0], r, c))
            sharks_cur_dir[value[0]] = value[1]
        
        # 2. 냄새 -1 해주기
        for i in range(N):
            for j in range(N):
                t_idx, t_time = grids[i][j]
                if t_time == 0: continue
                elif t_time == 1: grids[i][j] = (0, 0)
                else: grids[i][j] = (t_idx, t_time-1)

        if len(sharks_pos) == 1:
            print(time)
            break
    else: 
        print(-1)

if __name__ == "__main__":
    N, M, k = map(int, sys.stdin.readline().split())
    sharks_pos = []
    grids = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if temp[j] == 0:
                grids[i][j] = (0, 0)
            else: 
                sharks_pos.append((temp[j], i, j)) # 상어 번호, 위치r, 위치c
                grids[i][j] = (temp[j], k) # 상어들의 향수 시간 뿌리기
    # 상어의 현재 방향
    temp = list(map(int, sys.stdin.readline().split()))
    sharks_cur_dir = dict()
    for i in range(1, M+1):
        sharks_cur_dir[i] = temp[i-1]
    del temp
    # 상어의 방향
    sharks_dirs = [[0]] # [위, 아래, 왼쪽, 오른쪽]
    # 상어의 우선 순위 표
    for _ in range(M):
        temp = []
        for _ in range(4):
            temp.append(list(map(int, sys.stdin.readline().split())))
        sharks_dirs.append(temp)
    
    #### 모든 정보 print ##########
    # print("1. grids : ", grids)
    # print("2. shark_pos :", sharks_pos)
    # print("3. shark_cur_dir", sharks_cur_dir)
    # print("4. sharks_dir : ", sharks_dirs)

    shark_start()


"""
쓸데 없는 연산 빼기
def shark_start():
    global sharks_pos, sharks_cur_dir
    for time in range(1, 1001):
        # 1. 현재 위치에서 이동 -> 다음 이동할 위치
        boom_check = defaultdict(list) # 해당 위치에 boom 일어 났는지 check
        for idx, r, c in sharks_pos:
            cur_dir = sharks_cur_dir[idx]
            # 1-1. 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다
            #print("current shark num and current direction : ", idx, cur_dir)
            #print("current shark dir table : ", sharks_dirs[idx][cur_dir-1])
            for d in sharks_dirs[idx][cur_dir-1] :# 샤크 번호의 현재 바라보고 있는 방향의 우선순위
                nr, nc = r+dirs[d][0], c+dirs[d][1]
                if 0 <= nr < N and 0 <= nc < N and not grids[nr][nc][0]: # grids[nr][nc][0] = 냄새가 없다
                    boom_check[str(nr)+' '+str(nc)].append((idx, d)) # 새로운 방향 저장
                    break
            else: # 인접칸 다 돌았는데 갈 곳이 없다
                # 1-2. 자신의 냄새가 있는 칸의 방향으로 잡는다
                for d in sharks_dirs[idx][cur_dir-1] :
                    nr, nc = r+dirs[d][0], c+dirs[d][1]
                    if 0 <= nr < N and 0 <= nc < N and grids[nr][nc][0] == idx: # grids[nr][nc][0] = 자신의 냄새가 있는 칸
                        boom_check[str(nr)+' '+str(nc)].append((idx, d)) # 새로운 방향 저장
                        break
                else: # 그런데도 없으면 그냥 원래 정보 저장
                    boom_check[str(r)+' '+str(c)].append((idx, cur_dir))
        del sharks_pos
        #print("check 1 sharks move : ", boom_check)

        # 2. 냄새 -1 해주기
        for i in range(N):
            for j in range(N):
                t_idx, t_time = grids[i][j]
                if t_time == 0: continue
                elif t_time == 1: grids[i][j] = (0, 0)
                else: grids[i][j] = (t_idx, t_time-1)

        #print("check 2 grids : ", grids)
        
        # 3. 냄새 뿌리기 + boom check하면서
        sharks_pos = []
        #print("boom_check 2 : ", boom_check)
        for shark_r_c, shark_info in boom_check.items():
            r, c = map(int, shark_r_c.split())
            #print("boom > shark r and c : ", (r, c))
            #print("boom > sharkinfo", shark_info)
            if len(shark_info) == 1: # 해당 위치에 한마리 있는 거니까 냄새 바로 뿌리기
                shark_num, shark_new_dir = shark_info[0][0], shark_info[0][1]
            elif len(shark_info) > 1:
                temp = sorted(shark_info)
                #print("boom > shark info sort : ", temp)
                shark_num, shark_new_dir = temp[0][0], temp[0][1]
            else: continue
            sharks_pos.append((shark_num, r, c))# 상어 번호, 위치r, 위치c
            sharks_cur_dir[shark_num] = shark_new_dir # 상어의 현재 방향
            grids[r][c] = (shark_num, k)

        if len(sharks_pos) == 1:
            print(time)
            break
    else: 
        print(-1)
"""