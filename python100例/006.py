# 计算给定列表内数字的和
str = input('请以空格为间隔连续输入一个数组:')
lst = [int(n) for n in str.split()]
def get_lst_sum(lst):
    return print(sum(lst))
get_lst_sum(lst)