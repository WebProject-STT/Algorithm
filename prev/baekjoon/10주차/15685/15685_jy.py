# 드래곤커브(https://www.acmicpc.net/problem/15685)
import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    grids = [[False for _ in range(101)] for _ in range(101)]
    # x 축은 r 의미, y축은 c 의미
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    for _ in range(N):
        x, y, d, g = map(int, sys.stdin.readline().split())

        # 1. g세대까지 회전 방향 정하기
        curves = [d] # 0세대꺼
        for _ in range(g):
            temp = []
            for c in curves[::-1]:
                temp.append((c+1)%4)
            curves.extend(temp)
        
        # 2. curves 기준으로 이동한 부분 적기
        grids[x][y] = True
        for c in curves:
            next_x, next_y = x+dirs[c][0], y+dirs[c][1]
            if 0 <= next_x < 101 and 0 <= next_y < 101:
                grids[next_x][next_y] = True
                x, y = next_x, next_y

    # 3. 네꼭지점 모두 드래곤 커브 = 정사각형 개수 
    total = 0
    for r in range(100):
        for c in range(100):
            if grids[r][c] and grids[r+1][c] and grids[r][c+1] and grids[r+1][c+1]:
                total += 1

    print(total)