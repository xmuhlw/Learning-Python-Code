# 打印区间内的所有素数
# 素数:如果数字只能被1和自己整除就是素数
from re import L

from regex import I


m = int(input('请输入区间的左区间:'))
n = int(input('请输入区间的右区间:'))

def is_prime(i):
    
    if i in range(1,2):
        return True
    for idx in range(2,i):
        if i % idx == 0:
            return False
    else:
        return True
   
   
    
   

def print_primes(m,n): 
    for i in range(m,n+1):
        if is_prime(i):
            print(f'{i} is a prime')

print_primes(m,n)
    

