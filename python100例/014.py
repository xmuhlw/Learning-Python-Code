# 统计英文文章中每个单词的出现次数，主要用到的是字典
from multiprocessing.sharedctypes import Value
from pandas import value_counts


def get_count():
    with open('English_story.txt','r',encoding = 'utf-8') as f:
        count_word = {}
        for line in f:
            line = line[:-1]
            words = line.split()
            for word in words:
                if word not in count_word:
                    count_word[word] = 0
                count_word[word] += 1
    return count_word
count_word = get_count()
most_counst = sorted(count_word.items(), key = lambda x:x[1],reverse = True)
print(most_counst[:11])


    


