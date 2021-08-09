# 마라톤1
import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]

total = 0
for i in range(n - 1) : # 전체 길이
    x, y = d[i][0], d[i][1]
    nx, ny = d[i+1][0], d[i+1][1]
    total += abs(x-nx) + abs(y-ny)

answer = sys.maxsize
for i in range(1, n-1) :
    ox, oy = d[i-1][0], d[i-1][1]
    x, y = d[i][0], d[i][1]
    nx, ny = d[i+1][0], d[i+1][1]
    not_ignore = abs(ox-x) + abs(oy-y) + abs(x-nx) + abs(y-ny) # 제외하지 않았을 때
    ignore = abs(ox-nx) + abs(oy-ny) # 제외했을 때
    answer = min(answer, total - (not_ignore - ignore))

print(answer)


'''
def check(idx) :
    sum = 0
    nd = d[:idx] + d[idx+1:]
    for i in range(n-2) :
        x, y = nd[i][0], nd[i][1]
        nx, ny = nd[i+1][0], nd[i+1][1]
        sum += abs(x-nx) + abs(y-ny)
    return sum

if __name__ == "__main__" :
    input = sys.stdin.readline

    n = int(input())
    d = []
    for _ in range(n) :
        x, y = map(int, input().split())
        d.append((x, y))

    answer = sys.maxsize
    for i in range(1, n-1) :
        answer = min(answer, check(i))
    
    print(answer)
'''