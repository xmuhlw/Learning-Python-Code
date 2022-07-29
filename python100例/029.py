# 检索文本中的正确邮箱格式
content = '''
    寻隐者12345@qq.com不遇
    朝代:唐asdf12dsa#abc.com代
    作python666@163.cn者:贾岛
    松下问童子,言师python-abc@163com采药去。
    只有Python_ant-666@sina.net此山中,云深不知处 
'''

import re
pattern = re.compile(r'''
    [a-zA-Z0-9_-]+
    @
    [a-zA-Z0-9_-]+
    \.
    [a-zA-Z]{2,4}
''',
re.VERBOSE)
result = pattern.findall(content)
print(result)




