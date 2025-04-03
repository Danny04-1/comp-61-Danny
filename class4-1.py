# List Example
a = [1, 1, 2, 3, "shawn", True]
print(a[0])
print(a[2])

class studentinfo:
    def __init__(self,grade,student_id): 
        self.grade='F'
        self.student_id='-1'

student_class_dict={}
student_class_dict['jose']=studentInfo('A+', 123123)
student_class_dict['shawn']=studentInfo('C+', 454532)
student_class_dict['aaa']=studentInfo('B-', 234234)

for key, value in student_class_dict.items():
    if(value.grade=='F')
    print(value.student_id)
    print(key)
    



# Dictionary Example
students ={}
students = {}
students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}
students ['Shawn'] = {'Grade': 'F', 'StudentID': 00000}
students['aaa']={"Grade": 'A+', 'StudentID': 22322}
students['bbb']={"Grade": 'F', 'StudentID': 00000}
students['ccc']={'Grade': 'A+', 'StudentID': 22322}
students['ddd']={'Grade': 'F', 'StudentID': 00000}

for key, value in students.items():
    print(value)
    for info_key, info_value in value.items():
        if info_value == 'F':
            print(key)

print(students)
print('Jose:')
print(f' Grade: {students["Jose"]["Grade"]}')
print(f' ID: {students["Jose"]["StudentID"]}')

# Car Dictionary
car_dict = {
    'bmw': 1000,
    'ferrari': 2000,
    'ford': 3000
}

print(car_dict['bmw'])
print(car_dict['ferrari'])
print(car_dict['ford'])

print('-----------------')

for key, value

