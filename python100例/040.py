# 实现数组逆输出,reverse
a = [1,2,3,4,5,6,7,8,9]
for i in range(0,(len(a)+1)//2):
    temp = a[i]
    a[i] = a[len(a)-1-i]
    a[len(a)-1-i] = temp
print(a)


