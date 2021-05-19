# 점프

if __name__ == "__main__":
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N-1 and j == N-1:
                print(dp[i][j])
                break
            jump = maps[i][j]
            # 아래로 가는것
            if i+jump < N:
                dp[i+jump][j] += dp[i][j]
            # 오른쪽으로 가는 것
            if j+jump < N:
                dp[i][j+jump] += dp[i][j]