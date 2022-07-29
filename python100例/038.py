# Python提取人名

import jieba.posseg as posseg
import pandas as pd

with open('《鹿鼎记》.txt','r',encoding = 'utf-8') as f:
    content = f.read()
word_count = []
for word,flag in posseg.cut(content):
    if flag == 'nr':
        word_count.append(word)
print(pd.Series(word).value_counts()[:20])
