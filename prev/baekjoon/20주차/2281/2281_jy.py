# 데스노트
from sys import setrecursionlimit
setrecursionlimit(10**4+1)

dp = [[-1 for _ in range(1001)] for _ in range(1001)]

def dp_f(idx, col): # 현재 줄에서, 지금 까지 쓴 이름 길이 + 띄어쓰기
    
    if idx == n: return 0
    if dp[idx][col] > 0 : return dp[idx][col]

    dp[idx][col] = (m-col)**2 + dp_f(idx+1, names[idx])

    if col+1+names[idx] <= m:
        dp[idx][col] = min(dp[idx][col], dp_f(idx+1, col+1+names[idx]))
    
    return dp[idx][col]

if __name__ == "__main__":
    n, m = map(int, input().split())
    names = []
    for _ in range(n):
        names.append(int(input()))

    dp = [[0 for _ in range(m+1)] for _ in range(n)]

    print(dp_f(1, names[0]))

    print(dp)