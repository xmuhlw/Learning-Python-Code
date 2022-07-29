# 计算班级的高分低分平均分
# key:course , value:grade list
course_grades = {}
with open('course_student_grade_input.txt','r',encoding = 'utf-8') as f:
    for line in f:
        line = line[:-1]
        course,number,name,grade = line.split(',')
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))

for course,grade in course_grades.items():
    print(
        course,
        max(grade),
        min(grade),
        sum(grade)/len(grade)
    )
    

    
    



        




        

        
       
    


        

