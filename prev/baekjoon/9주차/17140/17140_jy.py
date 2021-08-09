# 이차원배열과 연산
import sys

def caculate(matrix, len_cur):
    #print("matrix : ", matrix)
    for idx, lines in enumerate(matrix):
        # 1. count
        temp = []
        for num in set(lines):
            if num:
                temp.append((num, lines.count(num)))
        matrix[idx] = []
        # 2. sort
        temp = sorted(temp, key=lambda x:(x[1], x[0]))
        len_line = len(temp)
        if len_line > 50: len_line = 50
        else: len_cur = max(len_cur, len_line*2)
        for i in range(len_line):
            matrix[idx].append(temp[i][0])
            matrix[idx].append(temp[i][1])
        
    # 0채우기
    for lines in matrix:
        for _ in range(len_cur-len(lines)):
            lines.append(0)
    #print("result : ", matrix, len_cur)
    return matrix, len_cur

if __name__ == "__main__":
    r, c, k = map(int, sys.stdin.readline().split())
    A = [tuple(map(int, sys.stdin.readline().split())) for _ in range(3)]

    len_cur_r, len_cur_c = 3, 3
    for time in range(101):
        if r-1 < len_cur_r and c-1 < len_cur_c: # 실제 현재 len보다 큰 r,c위치를 원할 수 잇기 때문
            if A[r-1][c-1] == k:
                print(time)
                break
        if len_cur_r >= len_cur_c:
            A, len_cur_c = caculate(A, len_cur_c)
        else:
            A, len_cur_r = caculate(list(zip(*A)), len_cur_r) # 결과를 보면 열 계산한 걸 행으로 append시켰기 때문에 다시 원위치
            A = list(zip(*A))
    else:
        print(-1)
    
