# 포도주 시식
import sys
N = int(sys.stdin.readline())
grapes = [0]+[int(sys.stdin.readline()) for _ in range(N)]
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    if i==1:
        dp[1] = grapes[1]
        continue
    if i==2:
        dp[2] = grapes[2]+grapes[1]
        continue
    dp[i] = max(dp[i-3]+grapes[i-1]+grapes[i], dp[i-1], dp[i-2]+grapes[i])
print(dp[N])