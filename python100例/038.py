# Python提取人名

import jieba.posseg as posseg
import pandas as pd

with open('《鹿鼎记》.txt','r',encoding = 'utf-8') as f:
    content = f.read()
words = []
for word,flag in posseg.cut(content):
    if flag == 'nr':
        words.append(word)
print(pd.Series(words).value_counts()[:20])
