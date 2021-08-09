# 2048(easy)
import sys
from collections import deque
N = int(sys.stdin.readline())

max_ = -sys.maxsize

grids = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def find_max(grid):
    global max_
    for g in grid:
        max_ = max(max_, max(g))
    return

def move_up(grid):
    for c in range(N):
        stack = []
        for r in range(N):
            if grid[r][c] and not stack: # 처음 만나는 숫자면
                stack.append([0, grid[r][c], False])
                if r: # 0번 인덱스가 아니면
                    grid[0][c] = grid[r][c]
                    grid[r][c] = 0
                continue
            if grid[r][c]:
                if stack[-1][1] == grid[r][c] and not stack[-1][2]: # 합쳐질 수 있으면
                    stack[-1][1] = stack[-1][1]*2
                    stack[-1][2] = True
                    grid[r][c] = 0
                    grid[stack[-1][0]][c] = stack[-1][1]
                else:
                    grid[stack[-1][0]+1][c] = grid[r][c]
                    if r != stack[-1][0]+1:  # 한칸차이 이상
                        grid[r][c] = 0
                    stack.append([stack[-1][0]+1, grid[stack[-1][0]+1][c], False])
                    
    return grid


def move_down(grid):
    for c in range(N):
        stack = []
        for r in range(-1, -N-1, -1):
            if grid[r][c] and not stack: # 처음 만나는 숫자면
                stack.append([-1, grid[r][c], False])
                if r != -1: # -1번 인덱스가 아니면
                    grid[-1][c] = grid[r][c]
                    grid[r][c] = 0
                continue
            if grid[r][c]:
                if stack[-1][1] == grid[r][c] and not stack[-1][2]:
                    stack[-1][1] = stack[-1][1]*2
                    stack[-1][2] = True
                    grid[r][c] = 0
                    grid[stack[-1][0]][c] = stack[-1][1]
                else:
                    grid[stack[-1][0]-1][c] = grid[r][c]
                    if r != stack[-1][0]-1:  # 한칸차이 이상
                        grid[r][c] = 0
                    stack.append([stack[-1][0]-1, grid[stack[-1][0]-1][c], False])
    return grid

def move_left(grid):
    for r in range(N):
        stack = []
        for c in range(N):
            if grid[r][c] and not stack: # 처음 만나는 숫자면
                stack.append([0, grid[r][c], False])
                if c: # -1번 인덱스가 아니면
                    grid[r][0] = grid[r][c]
                    grid[r][c] = 0
                continue
            if grid[r][c]:
                if stack[-1][1] == grid[r][c] and not stack[-1][2]:
                    stack[-1][1] = stack[-1][1]*2
                    stack[-1][2] = True
                    grid[r][c] = 0
                    grid[r][stack[-1][0]] = stack[-1][1]
                else:
                    grid[r][stack[-1][0]+1] = grid[r][c]
                    if c != stack[-1][0]+1:  # 한칸차이 이상
                        grid[r][c] = 0
                    stack.append([stack[-1][0]+1, grid[r][stack[-1][0]+1], False])
    return grid

def move_right(grid):
    for r in range(N):
        stack = []
        for c in range(-1, -N-1, -1):
            if grid[r][c] and not stack: # 처음 만나는 숫자면
                stack.append([-1, grid[r][c], False])
                if c != -1: # -1번 인덱스가 아니면
                    grid[r][-1] = grid[r][c]
                    grid[r][c] = 0
                continue
            if grid[r][c]:
                if stack[-1][1] == grid[r][c] and not stack[-1][2]:
                    stack[-1][1] = stack[-1][1]*2
                    stack[-1][2] = True
                    grid[r][c] = 0
                    grid[r][stack[-1][0]] = stack[-1][1]
                else:
                    t = grid[r][c]
                    grid[r][stack[-1][0]-1] = grid[r][c]
                    if c != stack[-1][0]-1:  # 한칸차이 이상
                        grid[r][c] = 0
                    stack.append([stack[-1][0]-1, grid[r][stack[-1][0]-1], False])
    return grid

def dfs(dfs_grid, n):
    if n == 5:
        find_max(dfs_grid)
        return
    dfs(move_up([g[:] for g in dfs_grid]), n+1)
    dfs(move_down([g[:] for g in dfs_grid]), n+1)
    dfs(move_left([g[:] for g in dfs_grid]), n+1)
    dfs(move_right([g[:] for g in dfs_grid]), n+1)

dfs(grids, 0)
# print(move_up([g[:] for g in grids]))
# print(move_down([g[:] for g in grids]))
# print(move_left([g[:] for g in grids]))
# print(move_right([g[:] for g in grids]))
print(max_)