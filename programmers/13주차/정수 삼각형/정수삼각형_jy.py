# 정수 삼각형

def solution(triangle):
    len_t = len(triangle)
    if len_t == 1: return triangle[0][0]
    dp = [[0 for _ in range(i+1)] for i in range(len_t)]
    dp[0][0] = triangle[0][0]
    # dp 구하기
    for i in range(1, len_t):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        dp[i][-1] = triangle[i][-1] + dp[i-1][-1]
        if i >= 2: # 사이 값들도 계산
            for j in range(1, i):
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]          
    
    return max(dp[-1])