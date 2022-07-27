# 计算班级的高分低分平均分
# key:course , value:grade list
course_grades = {}
with open('course_student_grade_input.txt','r',encoding = 'utf-8') as f:
    for fine in f:
        fine = fine[:-1]
        course,number,name,grade = fine.split(',')
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))
print(course_grades)


for course,grade in course_grades.items():
    print(
        course,
        max(grade),
        min(grade),
        sum(grade) / len(grade)
    )
