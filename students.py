from presence import Presence

class Students:
    students = []

    def __init__(self, name: str, surname: str, presence: Presence):
        self.name = name
        self.surname = surname
        self.presence = presence

    def add_student(self):
        student_data = {
            'name': self.name,
            'surname': self.surname,
            'presence': self.presence
        }
        Students.students.append(student_data)

    def edit_presence(self, new_presence: Presence):
        for student_data in Students.students:
            if student_data['name'] == self.name and student_data['surname'] == self.surname:
                student_data['presence'] = new_presence
                break

    def export_to_txt():
        with open('C:\\Users\\jula\\Desktop\\uni\\plik.txt', 'w') as f:
            for student in Students.students:
                f.write(str(student) + "\n")

    def import_from_txt(path:str):
        file = open(path, 'r')

        for line in file.readlines():
            data = line.strip()
            Students.students.append(data)
