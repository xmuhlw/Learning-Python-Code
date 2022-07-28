# Python进行多种日期格式的标准化
content = '''
白日2021/05/26依山尽,黄2021.05.27河入海流
欲穷05-28-2020千里目,更上5/29/2020一层楼
'''
import re
content = re.sub(r'(\d{4})/(\d{2})/(\d{2})',r'\1-\2-\3',content)
content = re.sub(r'(\d{4})\.(\d{2})\.(\d{2})',r'\1-\2-\3',content)
content = re.sub(r'(\d{2})-(\d{2})-(\d{4})',r'\3-\1-\2',content)
content = re.sub(r'(\d{1})/(\d{2})/(\d{4})',r'\3-0\1-\2',content)
print(content)