# 징검다리
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

"""
def solution(stones, k):
    total = 0
    check_t = False
    while True:
        check = 0
        for idx in range(len(stones)):
            if check == k: break
            if not stones[idx]: 
                check += 1
                continue
            if stones:
                check = 0
                stones[idx] -= 1
        else:
            if check == k: continue
            total += 1
            continue
        break
    return total
"""