# 1, 2, 3, 더하기 5

testcase = int(input()) # testcase 수

num = 1000000009 # 조건에서 나누라고 한 값

dp = [[0] * 4 for _ in range(100001)]

# 1, 2, 3으로 시작 또는 끝나는 경우 (인덱스 번호 기준으로 1, 2, 3 계산)
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, 100001): # 모든 경우에 수에 대해 계산 (시간초과가 뜨지 않도록 하기 위해 각 자리에서도 조건대로 나눠줘야 함)
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % num
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % num
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % num

for _ in range(testcase):
    n = int(input())
    print(sum(dp[n]) % num)
