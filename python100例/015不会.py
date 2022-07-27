# 统计目录下所有文件的大小
import os
sum = 0
for file in os.listdir('.'):
    if os.path.isfile(file):
        size = os.path.getsize(file)
        sum += size
print(f'当前目录下所有文件的大小和为{sum/1000}kb')
