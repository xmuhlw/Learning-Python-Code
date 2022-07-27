# 数据合并以及关联
from posixpath import split


course_teacher_map = {}
with open('course_teacher.txt','r',encoding = 'utf-8') as f:
    for fine in f:
        fine = fine[:-1]
        course , teacher = fine.split(',')
        course_teacher_map[course] = teacher

with open('course_student_grade_input.txt','r',encoding = 'utf-8') as f:
    datas = []
    for fine in f:
        fine = fine[:-1]
        course,number,name,grade = fine.split(',')
        teacher = course_teacher_map.get(course)      
        data = course,teacher,number,name,grade
        datas.append(data)

with open('course_student_grade_output.txt','w',encoding = 'utf-8') as f:
    for data in datas:
        f.write(','.join(data) + '\n')
    pass

    