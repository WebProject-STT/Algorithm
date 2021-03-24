# 감시피하기
import sys
N = int(sys.stdin.readline())
S_r, S_c, T, O = [], [], [], []
grids = []
for i in range(N):
    temp = sys.stdin.readline().split()
    grids.append(temp)
    for j in range(N):
        if temp[j] == 'X':
            O.append(N*i+j)
            continue
        if temp[j] == 'T':
           T.append((i, j))
           continue
        
len_ = len(O)
visited = [0 for _ in range(len_)]

def check(temp_grid):
    for cur_r, cur_c in T:
        # 북 check
        for i in range(cur_r, -1, -1):
            if temp_grid[i][cur_c] == 'S': return False
            if temp_grid[i][cur_c] == 'O': break
        # 남 check
        for i in range(cur_r, N):
            if temp_grid[i][cur_c] == 'S': return False
            if temp_grid[i][cur_c] == 'O': break
        # 서 check
        for j in range(cur_c, -1, -1):
            if temp_grid[cur_r][j] == 'S': return False
            if temp_grid[cur_r][j] == 'O': break
        # 동 check
        for j in range(cur_c, N):
            if temp_grid[cur_r][j] == 'S': return False
            if temp_grid[cur_r][j] == 'O': break
    else:
        return True


def find_combi(cur, last):
    if cur == 2:
        temp_grid = copy_grid = [i[:] for i in grids]
        for i in range(len_):
            if visited[i]:
                temp_grid[O[i]//N][O[i]%N] = 'O'
        return check(temp_grid)
    
    for i in range(last+1, len_):
        if not visited[i]:
            visited[i] = 1
            if find_combi(cur+1, i): return True
            visited[i] = 0

for i in range(len_):
    visited[i] = 1
    if find_combi(0, i):
        print("YES")
        break
    visited[i] = 0
else:
    print("NO")