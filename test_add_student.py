import pytest
import System
import Professor

username = 'goggins'
password =  'augurrox'

stuName = 'hdjsr7'
courseName = 'comp_sci'

#pass
def test_add_student(grading_system):
    users = grading_system.users
    grading_system.login(username,password)
    grading_system.usr.add_student(stuName, courseName)
    grading_system.__init__()
    if users[stuName]['courses'][courseName] == courseName:
        assert True


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem