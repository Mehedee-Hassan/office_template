

# sotring index array based on strnig array

string_array = ["aa","zz","bb","csa"]
index_array = [0,1,2,3]
todo = sorted(index_array ,key=lambda x: string_array[x])

print(todo)
# output:
# [0, 2, 3, 1]



# string class ,operator overloading
class Student:
    def __init__(self, name, grade, marks):
        self.name = name
        self.grade = grade
        self.marks = marks

    def __repr__(self):
        return repr((self.name, self.grade, self.marks))

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student('Chetan', 'C', 50)
s2 = Student('Swathi', 'A', 90)
s3 = Student('Megha', 'B', 70)

student_objects = [s1, s2, s3]

sorted(student_objects)
