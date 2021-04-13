# 팔
import sys
L, R = sys.stdin.readline().split()
len_L, len_R = len(L), len(R)
if len_L != len_R:
    print(0)
else:
    count = 0
    for i in range(len_L):
        if L[i] == 8 and L[i] == R[i]: count += 1
        else:
            break
    print(count)