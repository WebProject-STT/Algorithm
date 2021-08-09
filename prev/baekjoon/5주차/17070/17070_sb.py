# 파이프 옮기기 1
import sys
input = sys.stdin.readline

n = int(input()) # 집의 크기
matrix = [(list(map(int, input().split()))) for _ in range(n)] # 빈 공간 0, 벽은 1로 들어옴
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)] 

dp[0][1][0] = 1 # 파이프 끝 좌표

for r in range(n) : 
    for c in range(2, n) :
        if matrix[r][c] == 0 : # 0 : 가로, 1 : 세로, 2 : 대각선
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2] # 가로 (가로, 대각선에서 올 수 있음)
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2] # 세로 (세로, 대각선에서 올 수 있음)
            if matrix[r-1][c] == matrix[r][c-1] == 0 :
                dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2] # 대각선 (가로, 세로, 대각선에서 올 수 있음)

print(sum(dp[-1][-1]))


''' dfs를 이용한 방법
# python3 63% 시간초과
# pypy3로 확인하면 통과됨.....😭

cnt = 0

def dfs(r, c, state) : # state 0 :가로, 1 : 세로, 2 : 대각선
    global cnt
    if r == n - 1 and c == n - 1 :
        cnt += 1
        return
    if state == 0 or state == 2 :
        if c + 1 < n and matrix[r][c+1] == 0 :
            dfs(r, c + 1, 0) # 가로 상태로 이동
    if state == 1 or state == 2 :
        if r + 1 < n and matrix[r+1][c] == 0 :
            dfs(r + 1, c, 1) # 세로 상태로 이동
    if state == 0 or state == 1 or state == 2 :
        if r + 1 < n and c + 1 < n :
            if matrix[r][c+1] == 0 and matrix[r+1][c] == 0 and matrix[r+1][c+1] == 0 :
                dfs(r + 1, c + 1, 2) # 대각선 상태로 이동


dfs(0, 1, 0) # 파이프 끝 좌표

print(cnt)

'''