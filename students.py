from presence import Presence

class Students:
    students = []

    def __init__(self, name: str, surname: str, presence: str):
        self.name = name
        self.surname = surname
        self.presence = presence

    @classmethod
    def add_student(cls, student):
        student_data = {
            'name': student.name,
            'surname': student.surname,
            'presence': student.presence
        }
        cls.students.append(student_data)

    @classmethod
    def edit_presence(cls, student, new_presence):
        for student_data in cls.students:
            if student_data['name'] == student.name and student_data['surname'] == student.surname:
                student_data['presence'] = new_presence
                break

    @staticmethod
    def export_to_txt(path='plik.txt'):
        with open(path, 'w') as f:
            for student in Students.students:
                f.write(f"{student['name']},{student['surname']},{student['presence']}\n")

    @staticmethod
    def import_from_txt(path='plik.txt'):
        Students.students.clear()
        with open(path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    student_data = {
                        'name': parts[0],
                        'surname': parts[1],
                        'presence': parts[2]
                    }
                    Students.students.append(student_data)
