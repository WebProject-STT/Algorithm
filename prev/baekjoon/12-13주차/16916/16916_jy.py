# 부분 문자열

def make_table(p):
    j, len_p = 0, len(p)
    table = [0]*len_p
    for i in range(1, len_p):
        while j > 0 and p[i] != p[j]: #j가 0이거나 두 문자가 같을때까지 반복
            j = table[j-1]
        if p[i] == p[j]: #i와 j의 문자가 같다면 j를 증가
            j += 1
            table[i] = j # i번째 요소에는 j를 저장
    return table

def KMP(s, p):
    table = make_table(p)
    j = 0
    len_p = len(p)-1
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]  # 패턴은 현재 문자열 인덱스 i와 동일 위치인 부분으로 돌아감
        if s[i] == p[j]:
            if j == len_p: # 전체 문자열 이 일치했다는 의미
                # j = table[j] # 이때 첫번째 인덱스 j-len_p+2
                return True
            else: # 일치했으니 패턴의 다음 문자열로 넘어감
                j += 1
    return False


if __name__ == "__main__":
    S = input()
    P = input()
    print(1 if KMP(S, P) else 0)


"""
문자열 s의 부분 문자열이란 문자열의 연속된 일부

"aek", "joo", "ekj"는 "baekjoon"의 부분 문자열
"bak", "p", "oone"는 부분 문자열이 아니다.
"""

"""
if __name__ == "__main__":
    S = input()
    P = input()
    print(int(P in S))
"""