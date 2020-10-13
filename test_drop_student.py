import pytest
import System
import Professor

username = 'goggins'
password =  'augurrox'

stuName = 'akend3'
courseName = 'comp_sci'

#pass
def test_drop_student(grading_system):
    users = grading_system.users
    grading_system.login(username,password)
    grading_system.usr.drop_student(stuName, courseName)
    grading_system.__init__()
    if courseName not in users[stuName]['courses']:
        assert False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem