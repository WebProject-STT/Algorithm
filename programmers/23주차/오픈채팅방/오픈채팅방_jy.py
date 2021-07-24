# 오픈 채팅방
def solution(record):
    answer = []
    info = dict() # key(uid), value(name)
    
    for rc in record:
        temp = rc.split() # 명령어, uid, 이름
        if temp[0] == 'Enter' or temp[0] == 'Change':
            info[temp[1]] = temp[2]
            if temp[0] == 'Enter':
                answer.append([temp[1], "님이 들어왔습니다."])
        else:
            answer.append([temp[1], "님이 나갔습니다."])

    for idx, record in enumerate(answer):
        answer[idx] = info[record[0]]+record[1]
    return answer

print(solution([
    "Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"
]))

"""
* 닉네임 중복 허용
닉네임 변경 방법
1. 채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
2. 채팅방에서 닉네임 변경
* 닉네임 변경 -> 기존 채팅방 메시지 닉네임도 전부 변경 됨

최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태
"""