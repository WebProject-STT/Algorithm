# 미세먼지 안녕!
# pypy로는 통과됨.. ㅠㅠㅠ

import sys

def dust() : # 미세먼지 확산
    temp[air_cleaner[0]][0] = -1
    temp[air_cleaner[1]][0] = -1
    for i in range(r) :
        for j in range(c) :
            if matrix[i][j] > 0 : # 0 보다 클 때
                if matrix[i][j] >= 5 : # 5로 나눴을 때 몫이 있으면
                    n = matrix[i][j]//5
                    cnt = 0
                    for k in range(4) : # 4 방향 확인하고 확산
                        nr , nc = i + d[k][0], j +d[k][1]
                        if 0 <= nr < r and 0 <= nc < c and matrix[nr][nc] != -1 :
                            temp[nr][nc] += n
                            cnt += 1
                    temp[i][j] += matrix[i][j] - (n * cnt)
                else :
                    temp[i][j] += matrix[i][j]

def clean() : # 공기청정기

    # 위쪽 구간
    for i in range(air_cleaner[0] - 1, 0, -1) :
        temp[i][0] = temp[i-1][0]
    for i in range(c-1) :
        temp[0][i] = temp[0][i+1]
    for i in range(air_cleaner[0]) :
        temp[i][c-1] = temp[i+1][c-1]
    for i in range(c - 1, 1, -1) :
        temp[air_cleaner[0]][i] = temp[air_cleaner[0]][i-1]
    
    # 아래쪽 구간
    for i in range(air_cleaner[1] + 1, r - 1) :
        temp[i][0] = temp[i+1][0]
    for i in range(c - 1) :
        temp[r-1][i] = temp[r-1][i+1]
    for i in range(r - 1, air_cleaner[1], -1) :
        temp[i][c-1] = temp[i-1][c-1]
    for i in range(c - 1, 1, -1) :
        temp[air_cleaner[1]][i] = temp[air_cleaner[1]][i-1]
    
    temp[air_cleaner[0]][1] = 0
    temp[air_cleaner[1]][1] = 0

    return temp

if __name__ == '__main__' :
    input = sys.stdin.readline
    r, c, t = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(r)]
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계 방향
    air_cleaner = []
    for i in range(r) :
        if matrix[i][0] == -1 :
            air_cleaner = [i, i+1]
            break

    temp = [[0]*c for _ in range(r)] # 확산된 후의 상태 기록
    dust()
    clean()
    for _ in range(t-1) :
        matrix = temp
        temp = [[0]*c for _ in range(r)] # 확산된 후의 상태 기록
        dust()
        clean()
        
    print(sum(map(sum, temp)) + 2)