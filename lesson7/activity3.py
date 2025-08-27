students = [[1, 'John', 'Grade 7'], [2, 'Elton', 'Grade 8'], [3, 'Rebecca', 'Grade 7']]

student_dict = {}

for i in students:
    student_dict[i[0]] = i[1:]
    
print(student_dict)