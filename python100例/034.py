# Python给文章中的手机号打马赛克效果
content = '''
白日136123402312790依山尽,黄12315197812河入海流
欲穷12345千里目,更上13315212312一层楼
'''

import re
pattern = r'(1[3-9])\d{9}'
print(re.sub(pattern,r'\1*********',content))
