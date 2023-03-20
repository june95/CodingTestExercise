def solution(m, musicinfos):
    ''' 프로그래머스 [3차]방금 그 곡 풀이'''
    answer = '(None)'
    play_time = 0            # 정답 곡 재생 시간 기억용
    
    for musicinfo in musicinfos:
        music_info_list = musicinfo.split(',')
        
        tmp = [int(music_info_list[i].split(':')[0])*60 + \
            int(music_info_list[i].split(':')[1]) for i in range(2)]
        tmp_play_time = tmp[1] - tmp[0]     #각 음악 play time
        
        # 음악 code(악보 정보)
        music_code = music_info_list[3].replace('C#', 'c').replace('D#', 'd')\
                        .replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        
        tmp_time = tmp_play_time    # 남은 시간 계산 위한 tmp_time
        play_code = []      # 재생 시간동안 총 code 내용 저장 list
        
        while tmp_time > 0:   
            if tmp_time < len(music_code):  # 남은 시간이 노래 재생 시간보다 짧을 경우
                play_code.extend(music_code[:tmp_time])  # 악보 처음부터 남은 시간까지 extend
            else:                           # 남은 시간이 노래 재생 시간보다 긴 경우
                play_code.extend(music_code)  # 악보 전체 extend
                
            tmp_time -= len(music_code)     # 남은 시간에서 악보 길이만큼 뺴준다.
        
        play_code = ''.join(play_code)      # list 형태의 재생 code -> 문자열
        
				# m도 악보와 마찬가지로 # 붙은 것 소문자로 바꿔준다.
        m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f')\
            .replace('G#', 'g').replace('A#', 'a')
        
        if m in play_code:                  # 재생된 코드 안에 m 문자열이 존재할 경우
            if tmp_play_time > play_time:   # 현재 곡의 재생 시간이 더 길 경우  
                play_time = tmp_play_time   # play_time 갱신
                answer = music_info_list[2] # 정답에 현재 곡 이름 저장
        
    return answer