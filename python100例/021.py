# 统计学生喜好次数

like_count = {}
with open('student_like.txt','r',encoding = 'utf-8') as f:
    for line in f:
        line = line[:-1]
        name,likes = line.split(' ')
        split_like = likes.split(',')
        for like in split_like:
            if like not in like_count:
                like_count[like] = 0
            like_count[like] += 1

print(f'学生喜好次数的统计为{like_count}')

