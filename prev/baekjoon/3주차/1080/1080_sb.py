# 행렬

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]

def change(i, j) : # 자리 변경
    for x in range(i, i+3) :
        for y in range(j, j+3) :
            a[x][y] = 1 - a[x][y]

cnt = 0
for i in range(n-2) : # 3*3 부분행렬의 시작을 (0,0) 자리를 검사하여 같은지 확인
    for j in range(m-2) :
        if a[i][j] != b[i][j] : # 다를 경우 원소 뒤집기
            cnt += 1
            change(i, j)

for i in range(n) : # a와 b 비교
    if a[i] != b[i] : # 다를 경우 -1 출력
        print(-1)
        break
else: # for문 정상 종료 => 모두 같으므로 cnt 출력
    print(cnt)
