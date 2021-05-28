def solution(msg):
    answer = []
    len_m = len(msg)
    alpha_dict = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    idx = 0

    while idx < len_m:
        temp = msg[idx]
        # 현재 문자 + 다음 문자가 단어 사전에 있는지 
        # 이때 하나씩 늘려가며 어디까지 있는지 확인하기
        for i in range(idx+1, len_m):
            if temp+msg[i] not in alpha_dict[27:]:
                alpha_dict.append(temp+msg[i])
                answer.append(alpha_dict.index(temp))
                idx = i
                break
            else:
                temp += msg[i]
        else:
            answer.append(alpha_dict.index(temp))
            break
    return answer


print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("Z"))


"""
1. 길이가 1인 모든 단어를 포함하도록 사전 초기화
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾음
3. w에 해당하는 사전의 색인 번호 출력, 입력에서 w 제거
4. 입력에서 처리되지 않는 다음 글자가 남아 있다면 c -> w+c에 해당되는 단어 사전 등록
5. 2번으로 돌아감

<<사전>>
1 2 3 4 ~ 25 26
A B C D   Y  Z

"""