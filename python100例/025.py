# 计算开始和结束范围内的所有日期
import datetime

def get_date_range(begin_time,end_time):
    data_list = []
    while begin_time <= end_time:
        data_list.append(begin_time)
        begin_time_obj = datetime.datetime.strptime(begin_time,'%Y-%m-%d')
        days1_timedelta = datetime.timedelta(days = 1)
        begin_time = ((begin_time_obj) + days1_timedelta).strftime('%Y-%m-%d')

    return data_list



begin_time = '2021-07-09'
end_time = '2021-08-01'
date_list = get_date_range(begin_time,end_time)
print(date_list)

