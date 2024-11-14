def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    #시간 초단위로 변환
    video_len = list(map(int, video_len.split(":")))
    sec_len = video_len[0]*60 + video_len[1]

    pos = list(map(int, pos.split(":")))
    sec_pos = pos[0]*60+pos[1]

    op_start = list(map(int, op_start.split(":")))
    sec_start = op_start[0]*60+op_start[1]

    op_end = list(map(int, op_end.split(":")))
    sec_end = op_end[0]*60+op_end[1]

    
    
    for i in commands:
        #오프닝 건너뛰기
        if sec_pos>=sec_start and sec_pos<=sec_end:
            sec_pos = sec_end        

        if i == "prev":
            sec_pos-=10
            if sec_pos<0:
                sec_pos = 0
        
        elif i == "next":
            sec_pos+=10
            if sec_pos>sec_len:
                sec_pos = sec_len

        if sec_pos>=sec_start and sec_pos<=sec_end:
            sec_pos = sec_end

        
    pos[0],pos[1] = divmod(sec_pos,60)

    answer = "%02d:%02d" %(pos[0],pos[1])
    return answer