class Student:    
    def __init__(self,age,height,weight):
        self.age=age
        self.height=height
        self.weight=weight
    def get_weight(self):
        return self.weight
    def get_height(self):
        return(self.height)
    def get_age(self):
        return(self.age)
    

class_a_students_number=int(input())
class_a_students=[]
class_a=[]
for i in range(0,3):
    class_a.append(input().split())
for j in range(0,class_a_students_number):
    age=int(class_a[0][j])
    height=int(class_a[1][j])
    weight=float(class_a[2][j])
    student=Student(age,height,weight)
    class_a_students.append(student)

weight_A=0
height_A=0
age_A=0
for student in class_a_students:
    weight_A+=student.get_weight()
    height_A+=student.get_height()
    age_A+=student.get_age()
mean_weight_A=weight_A/class_a_students_number
mean_height_A=height_A/class_a_students_number
mean_age_A=age_A/class_a_students_number

class_b_students_number=int(input())
class_b_students=[]
class_b=[]
for i in range(0,3):
    class_b.append(input().split())
for j in range(0,class_b_students_number):
    age=int(class_b[0][j])
    height=int(class_b[1][j])
    weight=float(class_b[2][j])
    student=Student(age,height,weight)
    class_b_students.append(student)

weight_B=0
height_B=0
age_B=0
for student in class_b_students:
    weight_B+=student.get_weight()
    height_B+=student.get_height()
    age_B+=student.get_age()
mean_weight_B=weight_B/class_b_students_number
mean_height_B=height_B/class_b_students_number
mean_age_B=age_B/class_b_students_number

print(mean_age_A)
print(mean_height_A)
print(mean_weight_A)
print(mean_age_B)
print(mean_height_B)
print(mean_weight_B)

if mean_height_A>mean_height_B:
    print('A')
elif mean_height_A<mean_height_B:
    print('B')

elif mean_weight_A>mean_weight_B:
    print('B')
elif mean_weight_A<mean_weight_B:   
    print('A')
else:
    print('Same')    


