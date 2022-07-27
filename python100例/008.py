# 移除列表中的指定的多个元素
str1 = input('请以空格为间隔连续输入一个原始数组:')
lst1 = [int(n) for n in str1.split()]
str2 = input('请以空格为间隔连续输入一个删除指定元素的数组:')
lst2 = [int(n) for n in str2.split()]

data = [n for n in lst1 if n not in lst2]
print(
f'最终数组为{data}'
) 