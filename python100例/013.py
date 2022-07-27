# 统计学生成绩文件的最高分、最低分以及平均分
# 读取数据文件
from attr import field
from matplotlib.pyplot import get
from sklearn.metrics import average_precision_score


def read_file():
    with open('student_grade_input.txt','r',encoding = 'utf-8') as f:
        score = []
        for line in f:
            line = line[:-1]
            fields = line.split(',')
            score.append(int(fields[-1]))
    return score

datas = read_file()

# 计算数据
def get_grade(datas):
    max_grade = max(datas)
    min_grade = min(datas)
    avg_grade = round(sum(datas) / len(datas),2)
    return max_grade,min_grade,avg_grade
datas = get_grade(datas)

# 数据输出
print(f'max_grade:{datas[0]},min_grade:{datas[1]},avg_grade:{datas[-1]}')
