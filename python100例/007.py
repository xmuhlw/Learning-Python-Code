# 计算给定区间的所有偶数
begin = int(input('请输入左区间:'))
end = int(input('请输入右区间:'))

def print_even(begin,end):
    lst = []
    for i in range(begin,end+1):
        if i % 2 == 0:
            lst.append(i)
    print(f'区间内的偶数为{lst}')

print_even(begin,end)