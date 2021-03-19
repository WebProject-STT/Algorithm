# 스티커
import sys
input = sys.stdin.readline

t = int(input()) # testcase
d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위쪽부터 시계 방향

for _ in range(t) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    arr[0][1] += arr[1][0]
    arr[1][1] += arr[0][0]
    for i in range(2, n) :
        arr[0][i] += max(arr[1][i-1], arr[1][i-2])
        arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    print(max(arr[0][n-1], arr[1][n-1]))