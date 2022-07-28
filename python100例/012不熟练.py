# 读取成绩文件排序数据
# 读取文件 Student_grade_input.txt

# 读取文件
with open('Student_grade_input.txt','r',encoding = 'utf-8') as f:
    result = []
    for line in f:
        line = line[:-1]
        result.append(line.split(','))

# 数据排序
result_list = sorted(result, key = lambda x:int(x[2]),reverse = True)

# 数据写入
with open('Student_grade_output.txt','w',encoding = 'utf-8') as f:
    for data in result_list:
        f.write(','.join(data) + '\n')

        
        