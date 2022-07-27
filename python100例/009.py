# 对列表元素去重复
str = input('请以空格为间隔连续输入一个数组:')
lst = [int(n) for n in str.split()] 
# def clear_lst(lst):
#     new_lst = []
#     for i in lst:
#         if i not in new_lst:
#             new_lst.append(i)
#     return print(f'去重后的数组为{new_lst}')

# clear_lst(lst)

# 还可以用set的特性，直接用set(lst)可以达到相同的效果
lst = set(lst)
print(lst)