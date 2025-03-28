# 클래스(날짜 시간) 불러오기
import datetime

now = datetime.datetime.now()
print("현재시간 : ",now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 시간이 12 이상이면 오후, 12 미만이면 오전이라고 시간 출력
# 13시 -> 오후 1시
# 9시 -> 오전 9시
# 15시 -> 오후 3시
hour = now.hour
min =now.minute
if hour >= 12 :
    print("오후 {:02d}:{:02d}".format(hour-12,min))
else :
    print("오전 {:02d}:{:02d}".format(hour,min))

# 2025-03-27
print("{}-{:02d}-{}".format(now.year,now.month,now.day))