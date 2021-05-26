# 자원 캐기

if __name__ == "__main__":
    N, M = map(int, input().split())

    boards = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0][0] = boards[0][0]

    # 초기화 : 동 방향 / 남 방향
    for i in range(1, M):
        dp[0][i] = dp[0][i-1] + boards[0][i]
    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + boards[i][0]
    
    # dp
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + boards[i][j]
    
    print(dp[-1][-1])