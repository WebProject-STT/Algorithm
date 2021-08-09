# 마라톤 1
import sys
N = int(sys.stdin.readline())
nums = []

total = 0
for i in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))
    if i > 0:
        total += (abs(nums[i-1][0] - nums[i][0])+abs(nums[i-1][1] - nums[i][1]))

max_= 0
for i in range(1, N-1):
    # 두 점 사이간
    d1 = (abs(nums[i-1][0]-nums[i][0]) + abs(nums[i-1][1] - nums[i][1])) + (abs(nums[i][0]-nums[i+1][0]) + abs(nums[i][1] - nums[i+1][1]))
    # 건너 뛰어서
    d2 = abs(nums[i-1][0]-nums[i+1][0]) + abs(nums[i-1][1] - nums[i+1][1])
    max_ = max(max_, d1-d2)

print(total - max_)