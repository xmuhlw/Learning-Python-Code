# 有一个已经排好序的数组，现在输入一个数，要求按照原来的规律将它插入数组
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的情况，插入后此元素之后的数，依次往后移动一个
a = [1,3,5,9,13,15,28,100,0] # len(a) = 9
for i in range(0,len(a)-1):print(a[i],end = ' ')
print()
number = int(input('Please input the number you want to insert:'))
local = 0
for i in range(len(a)-2,-1,-1):
    if number > a[i]:
        local = i + 1
        break

for i in range(len(a)-1,local-1,-1):
    a[i] = a[i-1]
a[local] = number
for i in range(0,len(a)):print(a[i],end = ' ')
print()