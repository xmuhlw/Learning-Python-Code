# 求前N个数字的平方和

number = int(input('请输入数字:'))
def get_number_square(number):
    result = 1 
    while number > 1:
        result = result + number*number
        number -= 1
    return print(result)
get_number_square(number)