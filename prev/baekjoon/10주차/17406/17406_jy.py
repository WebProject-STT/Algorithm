# 배열 돌리기 4
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def rotation(order_idx, temp_A):
    # 가운데는 그대로 for문은 s만큼
    r, c, s = C[order_idx]
    #print("r, c", (r, c))
    for i in range(1, s+1):
        # 1. 동 방향 회전
        check = i*2
        cur_r, cur_c = r-i, c-i
        #print(cur_r, cur_c)
        next_v = temp_A[cur_r][cur_c]
        temp_A[cur_r][cur_c] = temp_A[r-s+1][c-s]
        for d in range(4):
            for _ in range(check):
                cur_r, cur_c = cur_r + dirs[d][0], cur_c + dirs[d][1]
                #print((cur_r, cur_c), end= " ")
                next_v, temp_A[cur_r][cur_c] = temp_A[cur_r][cur_c], next_v 
            #print()
        #print("##################################")
                
    return temp_A

def dfs(cur_num, orders=[]):
    global min_
    if cur_num == K:
        #print(orders)
        temp_A = [a[:] for a in A]
        for order_idx in orders:
            temp_A = rotation(order_idx, temp_A)
        for temp in temp_A:
            min_ = min(min_, sum(temp))
        return

    for i in range(K):
        if not visited[i]:
            orders.append(i)
            visited[i] = 1
            dfs(cur_num+1, orders)
            visited[i] = 0
            orders.pop()


if __name__ == "__main__":
    min_ = 250000
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    C = [] #회전 연산 정보
    for _ in range(K):
        r, c, s = map(int, input().split())
        C.append((r-1, c-1, s))
    # 회전에 대한 dfs -> 순열 (0, 1)이랑 (1, 0) 결과값 다르니꼐~~
    visited = [0]*K
    dfs(0)
    print(min_)
"""
배열 돌리기 4
N*M A 배열
A 배열의 값 - 각 행에 있는 모든 수의 합 중 최솟 값
배열 회전 연산 
    - (r, c, s)
    - (r-s, c-s) (r-s, c+s)
      (r+s, c-s) (r+s, c+s) 이런 정사각형을 시계방향으로 한칸씩 돌림
    - 회전은 네모
사용 가능한 회전 연산이 주어졌을때 배열 A의 최솟값을 구하라
[이때 회전 연산의 순서는 상관 X] => dfs
"""

