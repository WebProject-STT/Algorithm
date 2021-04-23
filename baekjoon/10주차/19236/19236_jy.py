import sys

# 반시계방향
dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
max_eat = 0
visited = [[0 for _ in range(4)] for _ in range(4)]

def fish_move(tgrids, tfish_infos, shark_r, shark_c):
    for j in range(1, 17):
        r, c = tfish_infos[j]
        if r == -1: continue
        idx, f_dir = tgrids[r][c]
        for i in range(8):
            d = (f_dir+i)%8
            nr, nc = dirs[d][0]+r, dirs[d][1]+c
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr != shark_r or nc != shark_c):
                if tfish_infos[tgrids[nr][nc][0]][0] != -1:
                    tfish_infos[idx], tfish_infos[tgrids[nr][nc][0]] = tfish_infos[tgrids[nr][nc][0]], tfish_infos[idx]
                else:
                    tfish_infos[idx] = [nr, nc]
                tgrids[nr][nc], tgrids[r][c] = [idx, d], tgrids[nr][nc]
                break

    return tgrids, tfish_infos

def dfs(tgrids, tfish_infos, shark_r, shark_c, shark_dir, eats):
    global max_eat
    max_eat = max(max_eat, eats)

    # 1. 상어 먹음
    # 복사
    tgrids, tfish_infos = [t[:] for t in tgrids], [p for p in tfish_infos]
    tfish_infos[tgrids[shark_r][shark_c][0]] = [-1, -1]
    tgrids[shark_r][shark_c] = [0, 0]

    # 1. 물고기 움직임
    tgrids, tfish_infos = fish_move(tgrids, tfish_infos, shark_r, shark_c)

    # 2. 상어 움직임
    for i in range(1, 4):
        next_shark_r, next_shark_c = shark_r + i*dirs[shark_dir][0], shark_c + i*dirs[shark_dir][1]
        if 0 <= next_shark_r < 4 and 0 <= next_shark_c < 4 and tgrids[next_shark_r][next_shark_c][0] != 0:
            dfs(tgrids, tfish_infos, next_shark_r, next_shark_c, tgrids[next_shark_r][next_shark_c][1], eats+tgrids[next_shark_r][next_shark_c][0])

if __name__ == "__main__":
    grids = []
    fish_info = [[-1, -1]]+[-1]*16
    for i in range(4):
        temp = list(map(int, sys.stdin.readline().split()))
        new_temp = []
        for j in range(0, 8, 2):
            new_temp.append([temp[j], temp[j+1]-1]) # 0 = 물고기 번호, 1 = 방향
            fish_info[temp[j]]=[i,j//2]
        grids.append(new_temp)

    shark_r, shark_c= 0, 0
    shark_dir = grids[shark_r][shark_c][1]
    dfs(grids, fish_info, shark_r, shark_c, shark_dir, grids[shark_r][shark_c][0])

    print(max_eat)
    