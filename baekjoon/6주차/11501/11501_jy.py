# 주식
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    num = list(map(int, sys.stdin.readline().split()))
    total, max_ = 0, num[-1]
    for idx in range(N-2, -1, -1):
        if max_ < num[idx]:
            max_ = num[idx]
        else:
            total += (max_ - num[idx])
    print(total)