# 이차원 배열과 연산
import sys

# 연산함수
# A : NxN 배열, L : 행의 길이 (칼럼 개수)
def operation(A, L) :
    for idx, row in enumerate(A) :
        temp = []
        for n in set(row) : # 행의 중복을 제거한 후
            if n : # 0이 아닌 숫자면
                temp.append((n, row.count(n))) # 해당 숫자에 대한 값을 세어줌
        temp = sorted(temp, key = lambda x : (x[1], x[0])) # 개수, 숫자 순서로 정렬
        templen = len(temp)
        if templen > 50 : templen = 50 # 숫자의 개수는 100을 넘어가면 안됨
        L = max(L, templen * 2) # 행의 길이를 최대로 바꿔줌
        A[idx] = [] # A의 idx행 초기화
        for i in range(templen) : # A의 idx행 재구성
            A[idx].append(temp[i][0])
            A[idx].append(temp[i][1])
    
    # 최대 길이만큼 0 채우기
    for idx, row in enumerate(A) :
        for _ in range(L-len(row)) :
            A[idx].append(0)
    
    return A, L

if __name__=='__main__' :
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]

    rlen, clen = 3, 3
    for time in range(101) :
        if r <= rlen and c <= clen and A[r-1][c-1] == k :
            print(time)
            break
        if rlen >= clen : # R연산
            A, clen = operation(A, clen)
        else : # C연산
            A, rlen = operation(list(zip(*A)), rlen) # 행과 열을 전치시켜 함수를 실행한다.
            A = list(zip(*A)) # 행과 열을 원상태로 바꾼다.
    else : # 100초 동안 r행 c열이 k가 아닌 경우
        print(-1)


'''
크기가 3x3인 배열 A에 대해 1초가 지날 때마다 다음의 배열 연산이 적용된다.
- R연산 : 배열 A의 모든 행에 대해서 정렬 수행. 행의 개수 >= 열의 개수인 경우 적용
- C연산 : 배열 A의 모든 열에 대해서 정렬 수행. 행의 개수 < 열의 개수인 경우 적용
정렬을 할 때는 나온 횟수, 숫자순으로 한다.
ex) [3, 1, 1]
    -> [3, 1, 1, 2] (3이 1개, 1이 2개 있다는 의미)
    -> [2, 1, 3, 1, 1, 2] (2개 1개, 3이 1개, 1이 2개 있다는 의미)
연산을 통해 행 또는 열의 크기가 변하는데, 비어있는 칸은 0으로 채워준다.
행과 열의 크기가 100을 넘어가는 경우 처음 100개를 제외한 나머지는 버린다.
--- 입력
r, c, k는 A[r][c]에 들어있는 값이 k라는 조건
그 다음부터는 3x3 배열인 A에 대해 주어짐
--- 출력
A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간 출력
---
R연산을 기준으로 함수를 만든다.
C연산 수행 시 행렬을 전치시켜서 함수 수행 후 다시 원본으로 만들어준다.
A[r][c]에 들어있는 값이 k가 될 때까지 수행한다.
여기서 중요한 것은, r과 c가 1부터 시작한다는 점이다.
즉, A[r][c]는 r행 c열이므로 실제로 계산할 때는 A[r-1][c-1]이 k값이 될 때까지 수행한다.
100초가 지나도 r행 c열이 k가 되지 않으면 -1을 출력한다.
'''