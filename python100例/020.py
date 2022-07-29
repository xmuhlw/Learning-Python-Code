# 批量合并多个txt文件
# import os
# contents = []
# data_dir = './datas/many_texts'
# for file in os.listdir(data_dir):
#     file_path = f'{data_dir}/{file}'
#     if os.path.isfile(file_path) and file.endswith('.txt'):
#         with open(file_path,encoding = 'utf-8') as f:
#             contents.append(f.read())

# final_contents = '\n'.join(contents)
# with open('./datas/many_texts.txt','w',encoding = 'utf-8') as f:
#     f.write(final_contents)







# 批量合并多个txt文件
import os
dir_path = './datas/many_texts'
content = []
for file in os.listdir(dir_path):
    file_path = f'{dir_path}/{file}'
    if os.path.isfile(file_path) and file.endswith('.txt'):
        with open(file_path,'r',encoding = 'utf-8') as f:
            content.append(f.read())
final_content = '\n'.join(content)
with open('./datas/many_texts.txt','w',encoding = 'utf-8') as f:
    f.write(final_content)
    pass
