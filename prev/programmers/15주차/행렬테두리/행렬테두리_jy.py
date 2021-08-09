def solution(rows, columns, queries):
    answer = []
    # 각 위치 원소 값
    origin = [[columns*(i-1)+j for j in range(1, columns+1)] for i in range(1, rows+1)]
    maxs = (rows+1)*(columns+1)
    for idx, q in enumerate(queries):
        x1, y1, x2, y2 = q
        # 회전 시계 방향 : 동, 남, 서, 북
        # [1] 동 -> x1-1(행 고정) + (y1-1 ~ y2-1)
        min_x = maxs
        last = origin[x1][y1-1] # 마지막 값이 남음
        min_x = min(min_x, last)
        for i in range(y1-1, y2):
            last, origin[x1-1][i] = origin[x1-1][i], last
            min_x = min(min_x, last)
        # [2] 남 -> y2-1(열 고정) + (x1-1 ~ x2-1)
        for i in range(x1, x2):
            last, origin[i][y2-1] = origin[i][y2-1], last
            min_x = min(min_x, last)
        # [2] 서 -> x2-1(행 고정) + (y2-2 ~ y1-1)
        for i in range(y2-2, y1-2, -1):
            last, origin[x2-1][i] = origin[x2-1][i], last
            min_x = min(min_x, last)
        # [3] 북 -> y1-1(열 고정) + (x2-2 ~ x1)
        for i in range(x2-2, x1-1, -1):
            last, origin[i][y1-1] = origin[i][y1-1], last
            min_x = min(min_x, last)
        answer.append(min_x)
    
    return answer