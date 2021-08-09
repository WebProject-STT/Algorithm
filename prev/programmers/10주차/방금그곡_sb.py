def music_check(m, music, time) : # 악보 확인
    m = m.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'W').replace('A#', 'P')
    music = music.replace('C#', 'X').replace('D#', 'Y').replace('F#', 'Z').replace('G#', 'W').replace('A#', 'P')
    
    musiclen = len(music)
    music = time//musiclen*(music) + music[:time%musiclen]
    
    if m in music : return True
    
    return False

def solution(m, musicinfos):
    answer = ''
    musiclist = []

    minute = -1
    for musicinfo in musicinfos :
        musicinfo = musicinfo.split(',')
        start, end = list(map(int, musicinfo[0].split(':'))), list(map(int, musicinfo[1].split(':')))
        cur_minute = 60*(end[0] - start[0]) + end[1] - start[1]
        music = musicinfo[3]
        check = (music_check(m, music, cur_minute))
        if check :
            if minute < cur_minute :
                minute = cur_minute
                answer = musicinfo[2]

    if len(answer) == 0 :
        return "(None)"
    
    return answer