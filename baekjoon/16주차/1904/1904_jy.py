# 01 타일

if __name__ == "__main__":
    N = int(input())
    if N == 1: print(1)
    elif N == 2: print(2)
    else:
        dp = [0]*(N+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, N+1):
            dp[i] = (dp[i-2] + dp[i-1])%15746
        
        print(dp[-1])

