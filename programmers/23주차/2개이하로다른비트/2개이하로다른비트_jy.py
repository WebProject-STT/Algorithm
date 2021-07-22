def fx(num):
    len_n = len(num)

    # 전체 다 1이면 큰 수가 되기 위해, 맨 앞 1추가 + 바로 다음 0 변경(2개 다름) 나머지는 1 그대로
    if set(num) == {'1'}: 
        return int('10'+'1'*(len_n-1), 2)
    
    # 2진수에 0이 하나라도 포함이면 뒤에서부터 0이 나오는 지점 찾기 (1로 대체할 부분)
    for idx in range(len_n-1, -1, -1):
        if num[idx] == '0': break

    # num[idx+2:]는 무조건 다 1임
    # idx가 맨 마지막 인덱스면 뒤에 0 붙일 필요 x
    return int(num[:idx] + '10' + num[idx+2:], 2) if idx != len_n-1 else int(num[:idx] + '1', 2) 

def solution(numbers):
    answer = []
    for num in numbers:
        if num == 0: answer.append(1)
        elif num == 1: answer.append(2)
        else:
            answer.append(fx(bin(num)[2:]))
    return answer
