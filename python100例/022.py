# 如何获取当前的日期时间
import datetime
curr_datatime = datetime.datetime.now()
str_time = curr_datatime.strftime('%Y-%m-%D-%H-%M-%S')
print(str_time)
print(type(str_time))
print('year',curr_datatime.year)
print('month',curr_datatime.month)
print('day',curr_datatime.day)
print('hour',curr_datatime.hour)
print('minute',curr_datatime.minute)
print('second',curr_datatime.second)