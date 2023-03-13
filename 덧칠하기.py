def solution(n, m, section):
    answer = 1
    wall_num = section[0] + m 
    
    for i in range(1, len(section)):
        if section[i] < wall_num:
            continue
            
        wall_num = section[i] + m
        answer += 1
    
    return answer