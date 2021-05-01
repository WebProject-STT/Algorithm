# 후보키
from itertools import combinations

def solution(relation):
    answer = 0
    relation = list(zip(*relation))
    att_len, tu_len = len(relation), len(relation[0])
    
    # 한개 attribute일때
    temp = []
    for i in range(att_len):
        if len(set(relation[i])) == tu_len:
            answer += 1
        else: temp.append(i)
    print("temp : ", temp, answer)
    print("###################################3")
    # 여러 attribute
    att_len = len(temp)
    if att_len >= 2:
        keys = []
        for i in range(2, att_len+1):
            temp2 = set()
            for combi in combinations(temp, i):
                result = list(zip(*[relation[c] for c in combi]))
                if len(set(result)) == tu_len:
                    for k in keys: # 최소성 만족하는지 확인 작업
                        if k.issubset(set(combi)): break
                    else:
                        keys.append(set(combi))
                else: continue
        answer += len(keys)
    return answer


print(solution(
    [["100","ryan","music","2"],["100","ryan","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))

"""
def solution(relation):
    answer = 0
    relation = list(zip(*relation))
    att_len, tu_len = len(relation), len(relation[0])
    
    # 한개 attribute일때
    temp = []
    for i in range(att_len):
        if len(set(relation[i])) == tu_len:
            answer += 1
        else: temp.append(i)
    print("temp : ", temp, answer)
    print("###################################3")
    # 여러 attribute
    att_len = len(temp)
    if att_len >= 2:
        for i in range(2, att_len+1):
            temp2 = set()
            for combi in combinations(temp, i):
                result = list(zip(*[relation[c] for c in combi]))
                if len(set(result)) == tu_len:
                    answer += 1
                    for c in combi: temp2.add(c)
            temp = [t for t in temp if t not in temp2]
                    
    return answer
"""