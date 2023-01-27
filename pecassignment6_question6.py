

def Student_Info(student_id, student_name = '', student_class = ''):
    print('ID:',student_id)
    if student_name != '':print('Name:',student_name)
    if student_class != '':print('Class:', student_class)

Student_Info(5)
Student_Info(5, 's', 'ece')
Student_Info(5, student_class = 'ece')
Student_Info(5, student_name = 'rudra')