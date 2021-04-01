# 연산자 끼워넣기
import sys

def find_sum(cur, result) :
    global max_sum, min_sum
    if cur == n - 1:
        max_sum = max(max_sum, result)
        min_sum = min(min_sum, result)
        return
    for i in range(4) :
        if operators[i] > 0 :
            tmp = result
            if i == 0 : # 덧셈
                result += a[cur + 1]
            elif i == 1 : # 뺄셈
                result -= a[cur + 1]
            elif i == 2 : # 곱셈
                result *= a[cur + 1]
            else : # 나눗셈
                if result < 0 :
                    result = -(abs(result) // a[cur + 1])
                else : 
                    result //= a[cur + 1]
            operators[i] -= 1
            find_sum(cur + 1, result) # 변화된 result 적용
            operators[i] += 1
            result = tmp # 기존의 result 사용

if __name__ == "__main__" :
    inpput = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    operators = list(map(int, input().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈 개수

    INF = sys.maxsize
    max_sum = -INF
    min_sum = INF

    find_sum(0, a[0])

    print(max_sum)
    print(min_sum)