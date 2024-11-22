from students import Students
from presence import Presence

def print_student_list():
    for x in Students.students:
        print(x)

student1 = Students("Zuzia", "Wilk", Presence.present())
student2 = Students("Kinga", "Olczynska", Presence.absent())
student3 = Students("Oliwier", "Nowak", Presence.present())

Students.add_student(student1)
Students.add_student(student2)
Students.add_student(student3)

path = '/Users/ania/Desktop/uni/plik.txt'
Students.export_to_txt(path)
Students.import_from_txt(path)

print("Student list after import:")
print_student_list()

Students.edit_presence(student1, Presence.absent())
print('-' * 50)
print_student_list()