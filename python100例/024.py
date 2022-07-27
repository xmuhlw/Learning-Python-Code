# 计算任意日期N天前的日期
import datetime
def get_diff_days(pdate,days):
    pdate_obj = datetime.datetime.strptime(pdate,'%Y-%m-%d')
    print(type(pdate_obj))
    time_gap = datetime.timedelta(days = days)
    pdate_result = pdate_obj - time_gap
    print(type(pdate_result))
    return pdate_result.strftime('%Y-%m-%d')

print(get_diff_days('2022-04-28',7))
