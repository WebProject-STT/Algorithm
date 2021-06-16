# 퇴사

if __name__ == "__main__":
    N = int(input())

    tables = [list(map(int, input().split())) for _ in range(N)] # 0 - 기간, 1 - 금액

    dp = [0]*(N+1)
    
    for i in range(N-1, -1, -1):
        if i + tables[i][0] > N: dp[i] = dp[i+1]
        else:
            dp[i] = max(dp[i+1], tables[i][1] + dp[i+tables[i][0]])
    
    print(dp[0])