import pytest
import System
import Professor

username = 'akend3'
password = '123454321'

courseName = 'comp_sci'

#pass
def test_drop_student(grading_system):
    users = grading_system.users
    grading_system.login(username,password)
    grading_system.usr.view_assignments(courseName)
    grading_system.__init__()
    if users[username]['courses'][courseName] != courseName:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem