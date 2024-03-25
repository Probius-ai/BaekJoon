# 시간 입력받기
set_time = input().split()
# 시간 분단위 변환
total_time = int(set_time[0])*60+int(set_time[1])

# print(total_time)
# 시간 -45분 하기
want_time = total_time-45

#시간이 마이너스일 경우 +로
if want_time <0:
    want_time=24*60+want_time

# 알람 시간 설정,출력
alarm_time = [0,0]
alarm_time[0],alarm_time[1]= want_time//60, want_time%60

print(f"{alarm_time[0]} {alarm_time[1]}")