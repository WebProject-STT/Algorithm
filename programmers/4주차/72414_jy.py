def change_time(times):
    h, m, s = map(int, times.split(":"))
    return h*3600+m*60+s

def change_str(times):
    result = ''
    t_h = times//3600
    if t_h < 10: result += '0'+str(t_h)+':'
    else: result += str(t_h)+':'
    tt = times%3600
    t_m = tt//60
    if t_m < 10: result += '0'+str(t_m)+':'
    else: result += str(t_m)+':'
    t_s = tt%60
    if t_s < 10: result += '0'+str(t_s)
    else: result += str(t_s)
    return result

def solution(play_time, adv_time, logs):
    # 문자열 시간 변환
    play_time = change_time(play_time)
    adv_time = change_time(adv_time)
    logss = []
    start, end = [], []
    for log in logs:
        a, b = map(change_time, log.split("-"))
        logss.append(a)
        start.append(a)
        logss.append(b)
        end.append(b)
        print("pair : ", (a, b))
    logss.append(1300)
    start.append(1300)
    logss.append(3500)
    end.append(3500)
    logss.append(1560)
    start.append(1560)
    logss.append(2800)
    end.append(2800)
    logss = sorted(set(logss))
    
    if play_time == adv_time: return "00:00:00"
    len_ = len(logss)
    print(start)
    print(end)
    print(logss)
    # 첫번째 -> 재생 횟수 저장, 두번째 -> 초 단위 저장
    memories = [0 for _ in range(len_)]
    cnt = 0
    for idx in range(len_):
        if not idx: # 첫번째 원소이면
            count = 1
        if logss[idx] in end:
            count -= 1
        if logss[idx] in start and idx: 
            count += 1
            memories[idx]
        #memories[idx] = memories[idx-1] + 1
        if idx != len_-1:
            memories[idx] = ((logss[idx+1]-logss[idx])*count)
    print(memories)
    # 두번째 -> 누적 시간 계산
    for idx in range(1, len_):
        memories[idx] += memories[idx-1]
    print(memories)
    return

test_play = ["02:03:55", "99:59:59", "50:00:00"]
test_adv = ["00:14:15", "25:00:00", "49:00:00"]
test_logs = [["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
            , ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
            , ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]
test_result = ["01:30:59", "01:00:00", "00:00:00"]

print(solution(test_play[0], test_adv[0], test_logs[0]))