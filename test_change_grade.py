import pytest
import System
import Staff

username = 'cmhbf5'
password =  'bestTA'
studentName = 'akend3'
courseName =  'comp_sci'
assignName = 'assignment1'
grade = 95

#pass
def test_change_grade(grading_system):
    users = grading_system.users
    grading_system.login(username,password)
    grading_system.usr.change_grade(studentName,courseName,assignName,grade)
    grading_system.__init__()
    if users[studentName]['courses'][courseName][assignName]['grade'] == 0:
        assert True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem



