h,m = map(int,input().split())
time = h*60+m - 45
if time<0:
    time+=1440
print("{} {}".format(time//60,time%60))