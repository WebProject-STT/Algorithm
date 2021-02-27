# 1,2,3 더하기 5

# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
# 조건 : 연속 불가!!

temp = 1000000009

count = int(input())
nums = [int(input()) for _ in range(count)]
max_ = max(nums)
dp = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
if max_ > 3:
    for n in range(3, max_):
        dp.append([
            (dp[n-1][1] + dp[n-1][2]) % temp, # 1 연속
            (dp[n-2][0] + dp[n-2][2]) % temp, # 2연속
            (dp[n-3][0] + dp[n-3][1]) % temp # 3연속 
        ])

for num in nums:
    print(sum(dp[num-1])% temp)
