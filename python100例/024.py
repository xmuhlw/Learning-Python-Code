# 计算任意日期N天前的日期

import datetime
def get_diff_time(pdate,days):
    class_pdate = datetime.datetime.strptime(pdate,'%Y-%m-%d')
    gap_time = datetime.timedelta(days = days)
    diff_time = class_pdate - gap_time
    return diff_time.strftime('%Y-%m-%d')

print(get_diff_time('2022-07-29',7))
