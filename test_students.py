import os
from students import Students
from presence import Presence

TEST_FILE_PATH = "test_students.txt"

class TestONStudents:
    def test_add_student_success(self):
        # given
        student1 = Students("Ada", "Browska", Presence.present())
        Students.students = []

        # when
        Students.add_student(student1)

        # then
        expected = [{"name": "Ada", "surname": "Browska", "presence": Presence.present()}]
        assert Students.students == expected

    def test_edit_presence_success(self):
        # given
        student1 = Students("Ada", "Browska", Presence.present())
        Students.students = []
        Students.add_student(student1)

        # when
        Students.edit_presence(student1, Presence.absent())

        # then
        expected = [{"name": "Ada", "surname": "Browska", "presence": Presence.absent()}]
        assert Students.students == expected

    def test_export_to_txt_success(self):
        # given
        student1 = Students("Ada", "Browska", Presence.present())
        student2 = Students("Ola", "Nowak", Presence.absent())
        Students.students = []
        Students.add_student(student1)
        Students.add_student(student2)

        # when
        Students.export_to_txt(TEST_FILE_PATH)

        # then
        assert os.path.exists(TEST_FILE_PATH)
        with open(TEST_FILE_PATH, 'r') as f:
            lines = f.readlines()
        expected = "Ada,Browska,present\nOla,Nowak,absent\n"
        assert "".join(lines) == expected

    def test_import_from_txt_success(self):
        # given
        Students.students = []
        with open(TEST_FILE_PATH, 'w') as f:
            f.write("Ada,Browska,present\nOla,Nowak,absent\n")

        # when
        Students.import_from_txt(TEST_FILE_PATH)

        # then
        expected = [
            {"name": "Ada", "surname": "Browska", "presence": "present"},
            {"name": "Ola", "surname": "Nowak", "presence": "absent"}
        ]
        assert Students.students == expected


