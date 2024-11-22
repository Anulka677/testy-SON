import os
from students import Students
from presence import Presence

# Ścieżka testowego pliku
TEST_FILE_PATH = 'test_students.txt'


def setup_function():
    """Czyszczenie listy studentów przed każdym testem."""
    Students.students.clear()
    # Usuwanie pliku, jeśli istnieje
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)


def teardown_function():
    """Usuwanie testowego pliku po każdym teście."""
    if os.path.exists(TEST_FILE_PATH):
        os.remove(TEST_FILE_PATH)


def test_add_student():
    """Test dodawania studentów do listy."""
    student = Students("Ania", "Nowak", Presence.present())
    Students.add_student(student)
    assert len(Students.students) == 1
    assert Students.students[0]['name'] == "Ania"
    assert Students.students[0]['surname'] == "Nowak"
    assert Students.students[0]['presence'] == "present"


def test_edit_presence():
    """Test edycji obecności studenta."""
    student = Students("Ania", "Nowak", Presence.present())
    Students.add_student(student)
    Students.edit_presence(student, Presence.absent())
    assert Students.students[0]['presence'] == "absent"


def test_export_to_txt():
    """Test eksportu listy studentów do pliku."""
    student1 = Students("Ania", "Nowak", Presence.present())
    student2 = Students("Piotr", "Kowalski", Presence.absent())
    Students.add_student(student1)
    Students.add_student(student2)
    Students.export_to_txt(TEST_FILE_PATH)
    assert os.path.exists(TEST_FILE_PATH)
    with open(TEST_FILE_PATH, 'r') as file:
        content = file.readlines()
    assert len(content) == 2
    assert content[0].strip() == "Ania,Nowak,present"
    assert content[1].strip() == "Piotr,Kowalski,absent"


def test_import_from_txt():
    """Test importu listy studentów z pliku."""
    with open(TEST_FILE_PATH, 'w') as file:
        file.write("Ania,Nowak,present\n")
        file.write("Piotr,Kowalski,absent\n")
    Students.import_from_txt(TEST_FILE_PATH)
    assert len(Students.students) == 2
    assert Students.students[0]['name'] == "Ania"
    assert Students.students[0]['surname'] == "Nowak"
    assert Students.students[0]['presence'] == "present"
    assert Students.students[1]['name'] == "Piotr"
    assert Students.students[1]['surname'] == "Kowalski"
    assert Students.students[1]['presence'] == "absent"

