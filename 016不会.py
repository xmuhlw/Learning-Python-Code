# 按照文件后缀名来整理文件夹
import os
import shutil
dir = './arrange_dir'
for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    print(file,ext)
