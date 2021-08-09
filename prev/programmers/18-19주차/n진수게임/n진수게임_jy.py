# n 진수 게임

def solution(n, t, m, p):
    answer = '0'
    check = "0123456789ABCDEF"
    num = 1
    while len(answer) <= m*t+1:
        if num < n:
            answer += check[num%n]
        else:
            result = ""
            temp = num
            # 진수 변환!
            while temp >= n:
                result += check[temp%n]
                temp = temp//n
            # 진수 변환은 (몫 + 나머지 거꾸로 올라감)
            result = check[temp]+result[::-1]
            answer += result
        num += 1

    return answer[p-1::m][:t]

print(solution(16, 16, 2, 2))