# 경사로
import sys

# 지나갈 수 있는 길인지 확인하는 함수
# N : 길의 길이, L : 경사로 길이, route : 길
def check_route(N, L, route) :
    ramp = [0]*N # 경사로를 세웠는지 확인하기 위한 리스트
    for i in range(N-1) :
        if route[i] != route[i+1] : # 높이 차이가 있는 경우
            if abs(route[i] - route[i+1]) > 1 : # 높이 차이가 1이 아닌 경우
                return False
            else : # 높이 차이가 1인 경우
                if route[i] - route[i+1] == 1 : # 높은 칸에서 낮은 칸
                    if i+1+L > N : return False
                    check = route[i+1] # 경사로를 세울 수 있는 높이인지 확인용
                    for j in range(i+1, i+1+L) :
                        if ramp[j] or route[j] != check : return False
                        ramp[j] = 1
                elif route[i] - route[i+1] == -1 : # 낮은 칸에서 높은 칸
                    if i-L < -1 : return False
                    check = route[i]
                    for j in range(i, i-L, -1) :
                        if ramp[j] or route[j] != check : return False
                        ramp[j] = 1
    return True
                        
    

if __name__=="__main__" :
    input = sys.stdin.readline
    N, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0 # 지나갈 수 있는 길의 수 기록

    for r in matrix : # 행 확인
        if check_route(N, L, r) : cnt += 1

    for c in range(N) : # 열 확인
        if check_route(N, L, [matrix[r][c] for r in range(N)]) : cnt += 1
    
    print(cnt)

'''
N x N 크기의 지도에서 갈 수 있는 길을 찾는 문제
여기서 길은 한 행 또는 한 열을 의미하며, 길은 총 2N개 존재
칸의 높이가 같아야 길을 지나갈 수 있는데, 만약 높이가 다른 경우 경사로 설치
경사로 높이는 항상 1이며, 길이는 L. 개수는 매우 많음
경사로는 낮은 칸과 높은 칸을 연결하며, 아래 조건을 만족해야 함
 - 경사로는 낮은 칸에 놓으면 L개의 연속된 칸에 경사로의 바닥이 모두 접해야함
 - 낮은 칸과 높은 칸의 높이 차이는 1이어야 함
 - 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 함
아래의 경우 경사로를 놓을 수 없음
 - 경사로를 놓은 곳에 또 경사로를 놓는 경우
 - 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
 - 낮은 지점의 칸 높이가 모두 같지 않거나 L개가 연속되지 않는 경우
 - 경사로를 놓다가 범위를 벗어나는 경우
 ---
 길을 검사하는 함수를 만들고 한 행 또는 한 열을 넣어 검사를 한다.
'''