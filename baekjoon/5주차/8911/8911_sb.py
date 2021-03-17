# 거북이
import sys
input = sys.stdin.readline

t = int(input()) # testcase
d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 상 우 하 좌 (시계 방향으로)

for _ in range(t): 
    move = input() # 이동 정보 받아옴
    f = 0 # 거북이의 정면
    x, y = 0, 0 # 거북이 위치
    min_x, max_x, min_y, max_y = 0, 0, 0, 0 # 길이 구하기 위해 필요
    for m in move :
        if m == 'L' : # 왼쪽으로 90도 회전
            f = (f + 3) % 4
        elif m == 'R' : # 오른쪽으로 90도 회전
            f = (f + 1) % 4
        else :
            if m == 'F' : # 앞으로 이동
                x += d[f][0]
                y += d[f][1]
            elif m == 'B' : # 뒤로 이동
                x -= d[f][0]
                y -= d[f][1]
            # 이동 후 min, max 길이 확인
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        
    print((max_x - min_x) * (max_y - min_y)) # 거북이가 이동한 영역 넓이