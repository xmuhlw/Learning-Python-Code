import re
import pandas as pd
with open('English_stroy1.txt',encoding = 'utf-8') as fin:
    content  = fin.read()
    

# print(content.split(' ')) 
word = re.split(r'[\s.()-?\n]+',content)
print(pd.Series(word).value_counts()[:20])