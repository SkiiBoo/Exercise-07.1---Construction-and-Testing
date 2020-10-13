import pytest
import System
import Student


stuName = 'akend3'
password = '123454321'
course = 'comp_sci'
gradeCourse = "databases"

#pass
def test_check_grades(grading_system):
    users = grading_system.users
    grading_system.login(stuName,password)
    grades = grading_system.usr.check_grades(gradeCourse)
    grading_system.__init__()
    assignments = users[stuName]['courses'][course]
    studentsGrades = []
    for key in assignments:
        studentsGrades.append([key, assignments[key]['grade']])

    if grades != studentsGrades:
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem