# 计算开始和结束范围内的所有日期

import datetime
data_range = []
def get_date_range(begin_time,end_time):
    while begin_time <= end_time:
        data_range.append(begin_time)
        class_begin_time = datetime.datetime.strptime(begin_time,'%Y-%m-%d')
        date_gap = datetime.timedelta(days = 1)
        begin_time = (class_begin_time + date_gap).strftime('%Y-%m-%d')
begin_time = '2022-07-25'
end_time = '2022-07-29'
get_date_range(begin_time,end_time)
print(data_range)
       