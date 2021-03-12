# 광고 삽입

# 문자열 -> 시간 (초)
def secTime(time) :
    h, m, s = map(int, time.split(":"))
    return 3600 * h + 60 * m + s

# 시간(초) -> 문자열
def strTime(time) :
    result = ''
    for _ in range(2) :
        temp = time % 60
        if temp < 10 :
            result = ':0' + str(temp) + result
        else :
            result = ':' + str(temp) + result
        time //= 60
    if time < 10 :
            result = '0' + str(time) + result
    else :
        result = str(time) + result
    return result
    
def solution(play_time, adv_time, logs):
    answer = ''
    
    # 두 영상의 길이가 같으면 무조건 영상 시작점 반환
    if play_time == adv_time :
        return "00:00:00"
    
    play = secTime(play_time) # 동영상 재생시간 길이
    adv = secTime(adv_time) # 광고 재생시간 길이
    cnt = [0] * (play + 1) # 구간별 재생 횟수를 저장할 리스트
    
    # 로그에 기록된만큼 구간별 재생 횟수 증가
    for log in logs :
        start, end = log.split("-")
        start = secTime(start)
        end = secTime(end)
        cnt[start] += 1
        cnt[end] -= 1
        # for i in range(start, end) :
        #     cnt[i] += 1
    
    # cnt를 누적합을 이용해 만들기
    for i in range(1, play + 1) :
        cnt[i] += cnt[i - 1]
    
    # 동영상의 시작 위치에 광고가 있는 경우를 기준으로 sum_cnt 초기화
    sum_cnt = 0
    for i in range(adv) :
        sum_cnt += cnt[i]
    
    max_sum = sum_cnt
    start = 0
    
    for i in range(adv, play) :
        sum_cnt += cnt[i] - cnt[i - adv]
        if max_sum < sum_cnt :
            max_sum = sum_cnt
            start = i - adv + 1
    
    return strTime(start)