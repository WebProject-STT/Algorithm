# 2×n 타일링
# dp[n] = dp[n-1] + dp[n-2]

num = int(input())

if num < 3:
    print(num)
else:
    dp = [1, 2, 3]
    for i in range(4, num+1):
        dp.append((dp[i-3] + dp[i-2])%10007)
    print(dp[-1])