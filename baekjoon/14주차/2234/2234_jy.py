# 성곽
from collections import deque

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(r, c):
    global visitied
    queue = deque()
    queue.append([r, c])
    visitied[r][c] = count_room
    count = 1
    while queue:
        r, c = queue.popleft()
        for i in range(4): # 0 1 1 1 => 0인 방향으로만 갈 수 있다는 뜻
            if blocks[r][c][i] == '0':
                nr, nc = r+dirs[i][0], c+dirs[i][1]
                if not visitied[nr][nc]:
                    count += 1
                    visitied[nr][nc] = count_room
                    queue.append([nr, nc])
    return count

if __name__ == "__main__":
    m, n = map(int, input().split())

    blocks = []
    for _ in range(n):
        temp = list(map(int, input().split()))
        temps = []
        for t in temp:
            b = bin(t)[2:]
            len_b = len(b)
            if len_b < 4:
                temps.append('0'*(4-len_b)+b)
            else: temps.append(b)
        blocks.append(temps)

    visitied = [[0 for _ in range(m)] for _ in range(n)]
    check = []
    count_room, max_room = 0, 1
    # 방의 개수 + 최대 방의 크기
    for i in range(n):
        for j in range(m):
            if not visitied[i][j]:
                count_room += 1
                if blocks[i][j] == '1111':
                    visitied[i][j] = count_room
                    check.append(1)
                else:
                    result = bfs(i, j)
                    max_room = max(max_room, result)
                    check.append(result)
    print(count_room)
    print(max(check))


    # 벽 하나 허물다 => visited에 나는 각 번호를 매김
    broke_max_room = 0
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if blocks[i][j][k] == '1':  # 벽을 허물다 + 그 방향으로 한칸 갈 수 있음ㅇ을 확인한다
                    nr, nc = i+dirs[k][0], j+dirs[k][1]
                    if 0 <= nr < n and 0 <= nc < m:
                        idx1, idx2 = visitied[i][j], visitied[nr][nc]
                        if idx1 != idx2: # 번호가 달라야 다른 방을 의미하기 때문
                            broke_max_room = max(broke_max_room, check[idx1-1] + check[idx2-1])
    print(broke_max_room)