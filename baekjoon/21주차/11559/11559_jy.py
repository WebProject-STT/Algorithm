# 뿌요뿌요

"""
1. 뿌요 필드에 둠 => 상하좌우 4개 이상 뿌요 모임
                => 같은 색 뿌요들이 한꺼번에 사라짐

2. 위에 뿌요들이 중력을 받아 밑으로 떨어짐

3. 1반복

* 이때, 터질 수 있는 뿌요 그룹이 여러 개이면 동시에
터져야 함

=> 연쇄가 몇번 일어나는지

[색]
R : 빨, G: 초, B: 파, P:보, Y:노
"""


from collections import deque

def booms(i, j, color): # bfs 이용
    global visitied

    queue = deque()
    queue.append([i, j])

    boom_check = 0 # 4개 이상 연쇄인지 check
    boom_dirs = [] # boom 위치

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            next_r, next_c = r+dr, c+dc
            if 0 <= next_r < R and 0 <= next_c < C \
                and grids[next_r][next_c] == color \
                and visitied[next_r][next_c] == 0:
                    boom_check += 1
                    visitied[next_r][next_c] = 1
                    boom_dirs.append([next_r, next_c])
                    queue.append([next_r, next_c])

    if boom_check >= 4:
        for i, j in boom_dirs:
            grids[i][j] = '.'
        return 1

    return 0

if __name__ == "__main__":
   
    grids = [list(map(str, input().strip())) for _ in range(12)]
    R, C = 12, 6

    total_boom = 0
    while True:
        check_boom = 0
        # [1] boom 먼저
        visitied = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grids[i][j] != '.' and visitied[i][j] == 0:
                    result = booms(i, j, grids[i][j])
                    if result: # grids 변경 필요 + 연쇄 작용 일어남
                        check_boom += 1
        
        if not check_boom: # 연쇄 x => 끝남            
            print(total_boom)
            break 
        else:
            total_boom += 1

        # [2] boom 끝나면 이제 dowm
        for c in range(C):
            temp = []
            for r in range(R):
                if grids[r][c] in ('R', 'G', 'B', 'P', 'Y'):
                    temp.append(grids[r][c]) # ['Y', 'Y']이런식
            temp = ['.']*(R-len(temp)) + temp # 부족한 부분은 모두 '.'임
            for r in range(R):
                grids[r][c] = temp[r]