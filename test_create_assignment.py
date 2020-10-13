import pytest
import System
import Staff

username = 'cmhbf5'
password =  'bestTA'

dueDate = '10/14/20'
courseName =  'comp_sci'
assignName = 'final'
grade = 95

#pass
def test_create_assignment(grading_system):
    courses = grading_system.courses
    grading_system.login(username,password)
    grading_system.usr.create_assignment(assignName, dueDate, courseName)
    grading_system.__init__()
    if courses[courseName]['assignments'][assignName]['due_date'] != dueDate:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem