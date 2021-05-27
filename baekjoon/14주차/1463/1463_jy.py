# 1로 만들기

if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(0)
    elif N == 2 or N == 3:
        print(1)
    else:
        dp = [0]*(N+1)
        dp[2], dp[3] = 1, 1

        for x in range(4, N+1):
            temp1, temp2, temp3 = x, x, x
            # 1. x가 3으로 나눠지는지 확인
            if x % 3 == 0:
                temp1 = dp[x//3]
            if x % 2 == 0:
                temp2 = dp[x//2]
            temp3 = dp[x-1]
            
            dp[x] = min(temp1, temp2, temp3) + 1 # +1의 의미는 현재 위치에서 전꺼로 넘어가는데 이동
        print(dp[-1])