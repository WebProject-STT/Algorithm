# 드래곤 커브
import sys
input = sys.stdin.readline

def curve(x, y, d, g) :
    curve_list = [d] # 이동 방향 리스트
    for _ in range(g) :
        curve_len = len(curve_list)
        for i in range(curve_len-1, -1, -1) :
            curve_list.append((curve_list[i]+1)%4)
    
    matrix[x][y] = 1
    for c in curve_list :
        x, y = x + dist[c][0], y + dist[c][1]
        if matrix[x][y] == 0 : matrix[x][y] = 1
    
    return matrix

if __name__=="__main__" :
    matrix = [[0]*101 for _ in range(101)]
    N = int(input())
    dist = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    for _ in range(N) :
        x, y, d, g = map(int, input().split())
        matrix = curve(x, y, d, g)
    
    cnt = 0
    for r in range(100) :
        for c in range(100) :
            if matrix[r][c] and matrix[r][c+1] and matrix[r+1][c] and matrix[r+1][c+1] :
                cnt += 1
    
    print(cnt)


'''
0세대는 길이가 1인 선분이고, 1세대는 0세대를 시게방향으로 90도 돌려서 끝점에 붙인 형태
이런 식으로 g세대는 (g-1)세대를 시계방향으로 90도 돌린 후 끝점에 붙이며 진행됨
g세대를 알려면 그 전 세대에 대해 알아야 함
x, y, d, g => 시작행, 시작열, 시작방향, 세대
'''