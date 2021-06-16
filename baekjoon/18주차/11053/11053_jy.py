# 가장 긴 증가하는 부분 수열

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    dp = [0]*N
    dp[0] = 1
    for i in range(1, len(nums)):
        temp = 0
        for j in range(i):
            if nums[j] < nums[i] and temp < dp[j]: # 내 값 보다 작은 애들 중에서 가장 max 값을 가진 dp의 값
                temp = dp[j]
        dp[i] = temp+1 # 걔+1

    print(max(dp))
            