def solution(info, query):
    answer = []
    len_info = len(info)
    infos = dict()
    scores = set()

    for idx, i in enumerate(info):
        temp = i.split() # lang, job, career, food, score
        for t in temp:
            if t.isdigit():
                t = int(t)
                scores.add(t) # 점수 비교 (점수, 인덱스)

            if t not in infos.keys():
                infos[t] = {idx}
            else:
                infos[t].add(idx)

    scores = sorted(list(scores))
    len_s = len(scores)
    key = infos.keys()

    for q in query:
        temp = q.split(" and ")
        temp = temp[:-1] + temp[-1].split(" ")
        score = int(temp[-1])
        if scores[-1] < score: answer.append(0)
        else:
            if scores[0] >= score : people = set([i for i in range(len_info)])
            else:
                people = set()
                # binary search
                left, right = 0, len_s-1

                while right > left:
                    m = (left+right) // 2
                    if scores[m] >= score: right = m
                    else: left = m+1
                people = set()
                for i in range(left, len_s):
                    people |= (infos[scores[i]])
                
            for i in range(3, -1, -1):
                if temp[i] == '-': continue
                if temp[i] in key:
                    people &= infos[temp[i]]
                
                if not people:
                    answer.append(0)
                    break
            else:
                answer.append(len(people))

    return answer

print(solution([
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100","- and - and - and - 150"]))

"""
[해당 조건에 맞는 지원자가 몇 명]
[[info]]
개발언어 : cpp, java, python
직군 : backend, frontend
경력구분 : junior, senior
소울푸드 : chicken, pizza
점수 : 1 ~ 100000

[[query]]
[조건] "개발언어 and 직군 and 경력 and 소울푸드 X"
개발언어 : cpp, java, python, -
직군 : backend, frontend, -
경력구분 : junior, senior, -
소울푸드 : chicken, pizza, -
점수 (X): 1 ~ 100000

"cpp and - and senior and pizza 500"
개발 언어 - CPP, 
직군 - 상관X,
경력 - senior,
소울푸드 - pizza,
점수 - 500
"""


"""
def solution(info, query):
    answer = []
    len_info = len(info)
    infos = dict()
    scores = set()

    for idx, i in enumerate(info):
        temp = i.split() # lang, job, career, food, score
        for t in temp:
            if t.isdigit():
                t = int(t)
                scores.add(t) # 점수 비교 (점수, 인덱스)

            if t not in infos.keys():
                infos[t] = {idx}
            else:
                infos[t].add(idx)

    scores = sorted(list(scores))
    len_s = len(scores)
    print(scores)
    key = infos.keys()
    print(infos)

    for q in query:
        temp = q.split(" and ")
        temp = temp[:-1] + temp[-1].split(" ")
        score = int(temp[-1])
        # 쿼리 검사
        print(temp)
        people = set([i for i in range(len_info)])
        for i in range(4):
            if temp[i] == '-': continue
            if temp[i] in key and (people & infos[temp[i]]): people &= infos[temp[i]]
            else:
                answer.append(0)
                break
        else:
            print(people)
            if scores[-1] < score: answer.append(0)
            else:
                print(score)
                # binary search
                left, right = 0, len_s-1
        
                while right > left:
                    m = (left+right) // 2
                    if scores[m] >= score: right = m
                    else: left = m+1
                temp = set()
                for i in range(left, len_s):
                    temp |= (infos[scores[i]])
                
                print(people & temp)
                answer.append(len(people & temp))

    return answer
"""