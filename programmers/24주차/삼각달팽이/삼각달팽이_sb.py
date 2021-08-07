# 삼각 달팽이 (예전에 풀었던 코드 그대로 넣음..ㅎ)
def solution(n):
    answer = []
    triangle = [[0 for _ in range(i)] for i in range(1, n+1)]

    row, col, lt, end, start, count = n, n, 0, n-1, 0, 1
    maximum = sum(i for i in range(1, n+1))

    while True:
        if count > maximum:
            break
        for i in range(start, row):
            triangle[i][lt] = count
            count += 1
        lt += 1
        for i in range(lt, col):
            triangle[end][i] = count
            count += 1
        end -= 1
        col -= 2
        row -= 2
        for i in range(row, start, -1):
            rt = len(triangle[i]) - lt
            triangle[i][rt] = count
            count += 1
        start += 2
        row += 1
    for i in range(n):
        for j in range(len(triangle[i])):
            answer.append(triangle[i][j])
    return answer