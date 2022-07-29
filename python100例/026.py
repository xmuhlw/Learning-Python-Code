

# 将unix时间戳转换成日期格式
import datetime
unix_time = 1620747647
datetime_class = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_class.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_str)