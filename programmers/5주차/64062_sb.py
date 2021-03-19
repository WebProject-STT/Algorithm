def check(stones, mid, k) :
    cnt = 0
    for stone in stones :
        if (stone <= mid) :
            cnt += 1
            if cnt == k :
                return 1
        else :
            cnt = 0
    return 0
    
def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left <= right :
        mid = (left + right) // 2
        if check(stones, mid, k) :
            answer = mid
            right = mid - 1
        else :
            left = mid + 1
    return answer

''' 처음에 시도한 코드
def solution(stones, k):
    answer = 0
    while True :
        cnt = 0
        for i in range(len(stones)) :
            if cnt == k :
                break
            if stones[i] == 0:
                cnt += 1
                continue
            else :
                cnt = 0
            stones[i] -= 1
        else :
            if cnt == k :
                continue
            answer += 1
            continue
        break
    return answer
'''