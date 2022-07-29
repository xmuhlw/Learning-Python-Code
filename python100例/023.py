# 计算两个日期相隔的天数
import datetime
birthday_time = '2000-07-08'
curr_time = datetime.datetime.now()
class_birthday_time = datetime.datetime.strptime(birthday_time,'%Y-%m-%d') #strptime 将str转为class
print(type(curr_time),type(class_birthday_time))
minus_time = curr_time - class_birthday_time
print(f'距离出生已经过了{minus_time}')
