# 读取成绩文件排序数据
# 读取文件
def read_file():
    with open('student_grade_input.txt','r',encoding = 'utf-8') as f: 
        result = []
        for line in f:
            line = line[:-1] # 移除分隔符
            result.append(line.split(',')) # 用','进行分割数据
    return result
datas = read_file()
print(datas)
# 数据排序
def sort_grades(datas):
    return sorted(datas,key = lambda x: int(x[2]),reverse = True)
datas = sort_grades(datas)

# 输出文件
def write_file(datas):
    with open('student_grade_output.txt','w',encoding = 'utf-8') as f: 
        for data in datas:
            f.write(','.join(data) + '\n')

write_file(datas)
