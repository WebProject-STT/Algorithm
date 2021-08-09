# 순위 매기기
"""
[2, 2, 1, 3, 5]
1, 2, 2, 3, 5
1, 2, 3, 4, 5


1, 1, 1, 3, 4, 5
1, 2, 3, 4, 5, 6
"""
if __name__ == "__main__":
    N = int(input())
    scores = []
    for _ in range(N):
        scores.append(int(input()))

    scores.sort()
    numbers = [i for i in range(1, N+1)]
    total = 0
    for i, j in zip(scores, numbers):
        total += abs(i-j)
    
    print(total)