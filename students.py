from presence import Presence

class Students:
    students = []

    def __init__(self, name: str, surname: str, presence: str):
        self.name = name
        self.surname = surname
        self.presence = presence

    @classmethod
    def add_student(cls, student):
        for existing_student in cls.students:
            if existing_student['name'] == student.name and existing_student['surname'] == student.surname:
                raise ValueError("Student already exists")

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
                return
        raise ValueError("Student not found")

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
                if len(parts) != 3 or parts[2] not in ["present", "absent"]:
                    raise ValueError("Invalid file format")
                Students.students.append({
                    'name': parts[0].strip(),
                    'surname': parts[1].strip(),
                    'presence': parts[2].strip()
                })
