def solution(people, limit):
    answer = 0
    people.sort()
    if people[0] > limit: return 0
    len_p = len(people)
    left, right = 0, len_p-1
    while left <= right:
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else: 
            answer += 1
            right -=1
    return answer

print(solution([70, 80, 50], 100))

"""
효율성 하나 통과 x
def solution(people, limit):
    answer = 0
    people.sort()
    if people[0] > limit: return 0
    count = 0
    while people:
        if len(people) >= 2:
            if people[0] + people[-1] <= limit:
                answer += 1
                del people[0]
                del people[-1]
                continue
            if people[0] + people[-1] > limit: # 0번 자리 +1 마지막은 -1
                answer += 1
                del people[-1]
        else: 
            if people[0] <= limit:
                answer += 1
                del people[0]
            break
    return answer
"""