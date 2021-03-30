# 연산자 끼워넣기
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
cals = list(map(int, sys.stdin.readline().split()))
INF = sys.maxsize
max_ = -INF
min_ = +INF

def find_min_max(c_num_idx, result):
    global max_, min_
    if c_num_idx == N-1:
        max_ = max(max_, result)
        min_ = min(min_, result)
        return
    
    for i in range(4):
        temp = result
        if cals[i] > 0:
            if i == 0: # 더하기
                result += nums[c_num_idx+1]
            elif i == 1: # 빼기
                result -= nums[c_num_idx+1]
            elif i == 2: # 곱하기
                result *= nums[c_num_idx+1]
            else: # 나누기
                # 음수면
                if result < 0:
                    result = -(abs(result)//nums[c_num_idx+1])
                else: result = result//nums[c_num_idx+1]
            cals[i] -= 1
            find_min_max(c_num_idx+1, result)
            cals[i] += 1
            result = temp

find_min_max(0, nums[0])
print(max_, min_)


