# 对list列表元素进行排序



str = input('请以空格为间隔连续输入一个数组:')
lst = [int(n) for n in str.split()]
lst1 = sorted(lst)
lst2 = sorted(lst,reverse=True)
print(f'按照元素升序进行排序{lst1}')
print(f'按照元素降序进行排序{lst2}')