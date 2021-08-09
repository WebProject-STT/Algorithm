# 2xn 타일링

n = int(input())

num = 10007 # 조건

if n < 3:
    print(n)
else:
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n]%num)
