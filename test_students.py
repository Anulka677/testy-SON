import os
import pytest
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
        student2 = Students("Kasia", "Browska", Presence.absent())
        Students.students = []
        Students.add_student(student1)
        Students.add_student(student2)

        # when
        Students.export_to_txt(TEST_FILE_PATH)

        # then
        assert os.path.exists(TEST_FILE_PATH)
        with open(TEST_FILE_PATH, 'r') as f:
            lines = f.readlines()
        expected = "Ada,Browska,present\nKasia,Browska,absent\n"
        assert "".join(lines) == expected

    def test_import_from_txt_success(self):
        # given
        Students.students = []
        with open(TEST_FILE_PATH, 'w') as f:
            f.write("Ada,Browska,present\nKasia,Browska,absent\n")

        # when
        Students.import_from_txt(TEST_FILE_PATH)

        # then
        expected = [
            {"name": "Ada", "surname": "Browska", "presence": "present"},
            {"name": "Kasia", "surname": "Browska", "presence": "absent"}
        ]
        assert Students.students == expected

    def test_add_duplicate_student(self):
        # given
        student1 = Students("Ada", "Browska", Presence.present())
        Students.students = []
        Students.add_student(student1)

        # when / then
        with pytest.raises(ValueError, match="Student already exists"):
            Students.add_student(student1)

    def test_edit_presence_nonexistent_student(self):
        # given
        Students.students = []
        student = Students("Nonexistent", "Student", Presence.present())

        # when / then
        with pytest.raises(ValueError, match="Student not found"):
            Students.edit_presence(student, Presence.absent())

    def test_export_to_read_only_file(self):
        # given
        read_only_path = "read_only_test.txt"
        with open(read_only_path, 'w') as f:
            f.write("")
        os.chmod(read_only_path, 0o400)  #read-only file

        # when / then
        with pytest.raises(PermissionError):
            Students.export_to_txt(read_only_path)

        os.chmod(read_only_path, 0o600)  #restore permissions
        os.remove(read_only_path)

    def test_import_nonexistent_file(self):
        # given
        nonexistent_file = "nonexistent_file.txt"

        # when / then
        with pytest.raises(FileNotFoundError):
            Students.import_from_txt(nonexistent_file)

    def test_import_empty_file(self):
        # given
        with open(TEST_FILE_PATH, 'w') as f:
            f.write("")

        # when
        Students.import_from_txt(TEST_FILE_PATH)

        # then
        assert Students.students == []

    def test_import_invalid_format(self):
        # given
        with open(TEST_FILE_PATH, 'w') as f:
            f.write("Invalid,Format,Here")

        # when / then
        with pytest.raises(ValueError, match="Invalid file format"):
            Students.import_from_txt(TEST_FILE_PATH)
