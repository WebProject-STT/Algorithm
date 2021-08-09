# 평범한 배낭

if __name__ == "__main__":
    N, K = map(int, input().split())
    things = [list(map(int, input().split())) for _ in range(N)]
    bag = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, K+1):
            w, v = things[i-1][0], things[i-1][1]
            if j >= w:
                bag[i][j] = max(bag[i-1][j], v+bag[i-1][j-w])
            else:
                bag[i][j] = bag[i-1][j]
    print(bag[N][K])

"""
필요한 물건 = N개
각 물건의 무게 W와 가치 V => 가지고 가면 가치 V만큼 즐김
배낭 = K만큼 무게만 견딤
=> 준서가 최대한 즐거운 여행을 하기 위해 넣을 수 있는 물건들의 가치
=> DP
"""