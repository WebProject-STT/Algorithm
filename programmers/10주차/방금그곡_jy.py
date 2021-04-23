def init(musicinfos):
    new = []
    for mm in musicinfos:
        temp = mm.split(',')
        mmm = temp[3].replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'W').replace('A#', 'P')
        h1, m1 = map(int, temp[0].split(':'))
        h2, m2 = map(int, temp[1].split(':'))
        new.append([(h2*60+m2)-(h1*60+m1), temp[2], mmm])
    return new

def solution(m, musicinfos):
    m = m.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'W').replace('A#', 'P')
    musicinfos = init(musicinfos)
    max_len, max_title = -1, ''
    for music in musicinfos:
        len_m =len(music[2]) 
        if len_m < music[0]: # 음악 길이 < 재생된 시간
            temp = ''
            t1, t2 = music[0]//len_m, music[0]%len_m
            temp = music[2]*t1
            if t2: temp += music[2][:t2]
        else: # 음악 길이 > 재생된 시간
            temp = music[2][:music[0]]

        if m in temp: # 멜로디가 안에 있으면 후보군에 넣기
            if max_len < music[0]: # 라디오에서 재생된 길이가 제일 긴 음악 제목, 먼저 입력된 음악 제목 반환
                max_len = music[0]
                max_title = music[1]
        #print("max_", (max_len, max_title))
    if max_len == -1: return "(None)"
    else: return max_title

"""
네오 기억: 음악 끝 + 처음 부분
방금 그곡 : 음악 제목 + 재생 시작되고 끝난 시간 + 악보
악보 =  C, C#, D, D#, E, F, F#, G, G#, A, A#, B
음악 길이 < 재생된 시간 : 처음부터 반복 재생
음악 길이 > 재생된 시간 : 처음부터 ~ 재생한 길이 만큼
조건 일치 많으면 : 라디오에서 재생된 길이가 제일 긴 음악 제목 반환 -> 먼저 입력된 음악 제목 반환
없으면 : "(None)"
"""