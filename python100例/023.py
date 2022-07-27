# 计算两个日期相隔的天数
import datetime
birthday_time = '2000-07-08'
str_birthday_time = datetime.datetime.strptime(birthday_time,'%Y-%m-%d')

curr_time = datetime.datetime.now()

minus_datetime = curr_time - str_birthday_time
print(minus_datetime)
