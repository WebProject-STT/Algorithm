# 감시 피하기
# (i * n) + j 형태를 이용해서 조합 만들기
import sys
input = sys.stdin.readline

n = int(input())
matrix, t_list, o_list = [], [], []
for i in range(n) :
    temp = list(input().split())
    matrix.append(temp)
    for j in range(n) :
        if temp[j] == 'T' : # 선생님 위치
            t_list.append((i, j))
        elif temp[j] == 'X' : # 장애물을 설치할 수 있는 위치
            o_list.append((i * n) + j)

o_len = len(o_list)
visited = [0] * o_len

def check(cm) : # 모든 학생들이 감시로부터 피할 수 있는지 확인
    for r, c in t_list : # 선생님별로 상, 하, 좌, 우 확인
        for i in range(r-1, -1, -1) : # 상
            if cm[i][c] == 'O' : break
            elif cm[i][c] == 'S': return 0
        for i in range(r+1, n) : # 하
            if cm[i][c] == 'O' : break
            elif cm[i][c] == 'S' : return 0
        for i in range(c-1, -1, -1) : # 좌
            if cm[r][i] == 'O' : break
            elif cm[r][i] == 'S' : return 0
        for i in range(c+1, n) : # 우
            if cm[r][i] == 'O' : break
            elif cm[r][i] == 'S' : return 0
    return 1

def o_combinations(cnt, cur) : # 장애물에 대한 경우의 수
    if cnt == 2 : # 경우의 수가 3개 나오는 경우
        copy_matrix = [x[:] for x in matrix] # matrix 원본 유지를 위해 복사본 생성
        for i in range(o_len) :
            if visited[i] :
                o = o_list[i]
                copy_matrix[o//n][o%n] = 'O'
        return check(copy_matrix)
    
    for i in range(cur + 1, o_len) :
        if visited[i] == 0 :
            visited[i] = 1
            if o_combinations(cnt + 1, i) : 
                return 1
            visited[i] = 0

for i in range(o_len) : 
    visited[i] = 1
    if o_combinations(0, i) : 
        print("YES")
        break
    visited[i] = 0
else :
    print("NO")

