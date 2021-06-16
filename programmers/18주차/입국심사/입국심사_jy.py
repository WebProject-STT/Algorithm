# 입국심사
def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n # 최대 걸릴 시간

    while left <= right:
        mid = (left+right)//2
 
        count = 0
        for t in times:
            count += (mid//t) # 몫이 더 큰 수가 최적의 시간
            if count >= n: break # 인원수 범위 초과
        
        # n명을 심사 할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다.
        if count >= n:
            answer = mid
            right = mid - 1
        # 없는 경우
        elif count < n:
            left = mid + 1
    return answer

print(solution(6, [7, 10]))