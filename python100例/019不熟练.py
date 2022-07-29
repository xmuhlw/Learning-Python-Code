

# 数据合并以及关联
course_teacher_map = {}
with open('course_teacher.txt','r',encoding = 'utf-8') as f:
    for line in f:
        line = line[:-1]
        course, teacher = line.split(',')
        course_teacher_map[course] = teacher

with open('course_student_grade_input.txt','r',encoding = 'utf-8') as f:
    datas = []
    for line in f:
        line = line[:-1]
        course,number,name,grade = line.split(',')
        teacher = course_teacher_map.get(course)
        data = course,teacher,number,name,grade
        datas.append(data)
with open('course_student_grade_output.txt','w',encoding = 'utf-8') as f:
    for data in datas:
        f.write(','.join(data) + '\n')

        

