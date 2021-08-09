# 스타트와 링크
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
k = N // 2

min_ = 1000000000
visited = [0 for _ in range(N)]


def find_combi(cur_num, last_num):
    global min_
    if cur_num == k:
        start, link = [],[]
        for i in range(N):
            if visited[i]: start.append(i)
            else: link.append(i)
        s_score, l_score = 0, 0
        for player1 in start:
            for player2 in start:
                s_score += grid[player1][player2]
        for player1 in link:
            for player2 in link:
                l_score += grid[player1][player2]
        min_ = min(min_, abs(l_score-s_score))
        return

    for i in range(last_num+1, N):
        visited[i] = 1
        find_combi(cur_num+1, i)
        visited[i] = 0

# 나올 수 있는 순열 조합
visited[0] = 1
find_combi(1, 0)
visited[0] = 0
print(min_)