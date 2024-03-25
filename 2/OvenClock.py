# 시간 입력받기
set_time = input().split()
take_time = int(input())
# 시간 분단위 변환
total_time = int(set_time[0])*60+int(set_time[1])


# 걸리는 시간 추가하기
want_time = total_time+take_time

#시간이 24시간을 넘어가는 경우
if want_time >= 24*60:
    want_time= want_time-24*60

# 알람 시간 설정,출력
alarm_time = [0,0]
alarm_time[0],alarm_time[1]= want_time//60, want_time%60

print(f"{alarm_time[0]} {alarm_time[1]}")