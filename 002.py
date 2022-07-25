# 求输入数字的阶乘
number = int(input('请输入需要计算阶乘的数字:'))
def get_jiecheng(number):
    result = 1
    while number > 0:
        result = result * number
        number -= 1
    return result

print(get_jiecheng(number))


    
     
    
